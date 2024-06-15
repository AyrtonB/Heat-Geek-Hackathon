import requests
from fastapi import APIRouter

router = APIRouter(tags=["Analysis"])


@router.get("/heat-geek-address-lookup")
def get_heat_geek_address_details(address: str, postcode: str) -> dict:
    url = f'https://hackathonapis-35klfnb33a-ew.a.run.app/property_info/{address}/{postcode}'
    return requests.get(url).json()
