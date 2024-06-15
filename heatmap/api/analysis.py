import requests
from fastapi import APIRouter

from heatmap.definitions.analysis import OpexEstimate

router = APIRouter(tags=["Analysis"])


@router.get("/heat-geek-address-lookup")
def get_heat_geek_address_details(address: str, postcode: str) -> dict:
    url = f'https://hackathonapis-35klfnb33a-ew.a.run.app/property_info/{address}/{postcode}'
    return requests.get(url).json()


@router.get("/opex-estimate")
def get_opex_estimate(address: str, postcode: str, scops: float) -> OpexEstimate:
    return OpexEstimate(
        annual_heat_pump_elec_cost=123.45, annual_gas_boiler_counterfactual_cost=234.56, annual_carbon_kg_reduction=12.3
    )
