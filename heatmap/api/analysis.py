import datetime
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

from heatmap.analysis import get_opex_estimate_ts_df, load_temperature_s
from heatmap.db import get_records_within_dates
from heatmap.definitions.analysis import (
    HeatPumpTimeSeriesRecord,
    KeyValue,
    OpexEstimate,
)
from heatmap.definitions.timeseries import PowerCarbonIntensity

router = APIRouter(tags=["Analysis"])


load_dotenv()
DB_CONN_STR = os.environ['DB_CONN_STR']

engine = create_engine(url=DB_CONN_STR)
bound_sessionmaker = sessionmaker(engine)


@router.get("/heat-geek-address-lookup")
def get_heat_geek_address_details(address: str, postcode: str) -> dict:
    url = f'https://hackathonapis-35klfnb33a-ew.a.run.app/property_info/{address}/{postcode}'
    return requests.get(url).json()


@router.get("/opex-estimate")
def get_opex_estimate(
    min_scops: str = '3.5',
    annual_heat_kwh_consumption: float = 12000,
    heating_on_temperature=17.0,
    min_temp: float = -5,
    max_temp: float = 20,
    max_cop: float = 7.5,
    n_households: int = 1,
    elec_unit_rate: float = 246.4,  # octopus 12M elec unit rate in £/MWh
    elec_standing_charge: float = 0.3872,  # octopus 12M elec standing charge in £/day
    gas_unit_rate: float = 59.3,  # octopus 12M gas unit rate in £/MWh
    gas_standing_charge: float = 0.2998,  # octopus 12M gas standing charge in £/day
    gas_boiler_efficiency: float = 0.85,
    gas_boiler_gco2_per_kwh_delivered: float = 215,  # https://www.mittensheatpumps.co.uk/heat-pumps/oil-gas-electric-comparison
) -> list[OpexEstimate]:
    min_scops = [float(scop) for scop in min_scops.split(",")]

    temperature_fp = 'data/temperature_2020_2032.csv'
    s_temperature = load_temperature_s(temperature_fp)

    with bound_sessionmaker() as session:
        power_carbon_intensities = get_records_within_dates(
            session, datetime.datetime(2020, 1, 1), datetime.datetime(2023, 12, 31), PowerCarbonIntensity
        )
        s_carbon_intensity = pd.DataFrame([pci.model_dump() for pci in power_carbon_intensities]).set_index(
            'start_time'
        )['value']
        s_carbon_intensity.index = pd.to_datetime(s_carbon_intensity.index)

    n_years = (s_temperature.index[-1] - s_temperature.index[0]).total_seconds() / (365 * 24 * 3600)

    response_objs = []

    for min_scop in min_scops:
        df_opex_estimate_ts = get_opex_estimate_ts_df(
            s_temperature,
            min_scop,
            annual_heat_kwh_consumption,
            heating_on_temperature,
            min_temp,
            max_temp,
            max_cop,
            n_households,
        )

        common_dt_idx = df_opex_estimate_ts.index.intersection(s_carbon_intensity.index)

        annual_heat_pump_elec_load = df_opex_estimate_ts['elec_load_kwh'].sum() / n_years
        annual_heat_pump_elec_cost = (annual_heat_pump_elec_load * elec_unit_rate / 1e3) + (elec_standing_charge * 365)
        annual_heat_pump_gco2 = (
            df_opex_estimate_ts.loc[common_dt_idx, 'elec_load_kwh']
            .multiply(s_carbon_intensity.loc[common_dt_idx])
            .sum()
            / 3  # n_year of carbon intensity
        )
        annual_counterfactual_boiler_gas_load = annual_heat_kwh_consumption / gas_boiler_efficiency
        annual_counterfactual_boiler_gas_cost = (annual_counterfactual_boiler_gas_load * gas_unit_rate / 1e3) + (
            gas_standing_charge * 365
        )
        annual_counterfactual_boiler_gco2 = annual_heat_kwh_consumption * gas_boiler_gco2_per_kwh_delivered

        response_objs.append(
            OpexEstimate(
                min_scops=min_scop,
                annual=[
                    KeyValue(key="heat_pump_elec_cost", value=str(round(annual_heat_pump_elec_cost, 2))),
                    KeyValue(
                        key="gas_boiler_counterfactual_cost", value=str(round(annual_counterfactual_boiler_gas_cost, 2))
                    ),
                    KeyValue(
                        key="carbon_kg_reduction",
                        value=str(round((annual_counterfactual_boiler_gco2 - annual_heat_pump_gco2) / 1e3, 2)),
                    ),
                ],
                timeseries=df_opex_estimate_ts.resample('m').mean().reset_index().to_dict(orient='records'),
            )
        )

    return response_objs
