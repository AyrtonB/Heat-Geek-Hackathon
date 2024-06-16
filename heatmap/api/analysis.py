import requests
from fastapi import APIRouter

from heatmap.definitions.analysis import KeyValue, OpexEstimate
from heatmap.analysis import load_temperature_s, get_opex_estimate_ts_df


router = APIRouter(tags=["Analysis"])


@router.get("/heat-geek-address-lookup")
def get_heat_geek_address_details(address: str, postcode: str) -> dict:
    url = f'https://hackathonapis-35klfnb33a-ew.a.run.app/property_info/{address}/{postcode}'
    return requests.get(url).json()

@router.get("/opex-estimate")
def get_opex_estimate(
    min_scops: str = '3.5',
    annual_heat_kwh_consumption: float = 12000, 
    heating_on_temperature = 17.0,
    min_temp: float = -5,
    max_temp: float = 20,
    max_cop: float = 7.5,
    n_households: int = 1,
    elec_unit_rate: float = 246.4,  # octopus 12M elec unit rate in £/MWh
    elec_standing_charge: float = 0.3872,  # octopus 12M elec standing charge in £/day
    gas_unit_rate: float = 59.3,  # octopus 12M gas unit rate in £/MWh
    gas_standing_charge: float = 0.2998  # octopus 12M gas standing charge in £/day
    # TODO add standing charges
) -> list[OpexEstimate]:
    temperature_fp = 'data/temperature_2020_2032.csv'
    min_scops = [float(scop) for scop in min_scops.split(",")]
    s_temperature = load_temperature_s(temperature_fp)

    n_years = (s_temperature.index[-1]-s_temperature.index[0]).total_seconds() / (365 * 24 * 3600)

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
            n_households
        )

        annual_heat_pump_elec_load = df_opex_estimate_ts['elec_load_kwh'].sum()/n_years
        annual_heat_pump_elec_cost = (annual_heat_pump_elec_load * elec_unit_rate / 1e3) + (elec_standing_charge * 365)
        annual_counterfactual_boiler_gas_load = annual_heat_kwh_consumption/0.8
        annual_counterfactual_boiler_gas_cost = (annual_counterfactual_boiler_gas_load * gas_unit_rate / 1e3) + (gas_standing_charge * 365)
 
        response_objs.append(OpexEstimate(
            min_scops=min_scop,
            annual=[
                KeyValue(key="heat_pump_elec_cost", value=str(round(annual_heat_pump_elec_cost, 2))),
                KeyValue(key="gas_boiler_counterfactual_cost", value=str(round(annual_counterfactual_boiler_gas_cost, 2))),
                KeyValue(key="carbon_kg_reduction", value=str(123.45))
            ]
        ))

    return response_objs
