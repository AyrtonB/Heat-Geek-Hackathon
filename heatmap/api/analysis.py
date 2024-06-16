import requests
from fastapi import APIRouter

from heatmap.definitions.analysis import KeyValue, OpexEstimate

router = APIRouter(tags=["Analysis"])


@router.get("/heat-geek-address-lookup")
def get_heat_geek_address_details(address: str, postcode: str) -> dict:
    url = f'https://hackathonapis-35klfnb33a-ew.a.run.app/property_info/{address}/{postcode}'
    return requests.get(url).json()


@router.get("/opex-estimate")
def get_opex_estimate(annual_heat_kwh_consumption: float, scops: str) -> list[OpexEstimate]:
    scops = [float(scop) for scop in scops.split(",")]
    return [
        OpexEstimate(
            annual=[
                KeyValue(key="heat_pump_elec_cost", value=str(annual_heat_kwh_consumption * scop * 0.15)),
                KeyValue(key="gas_boiler_counterfactual_cost", value=str(annual_heat_kwh_consumption * scop * 0.25)),
                KeyValue(key="carbon_kg_reduction", value=str(annual_heat_kwh_consumption * scop * 0.05))
            ]
        ) for scop in scops
    ]
