import datetime

from fastapi import APIRouter

from heatmap.definitions.timeseries import PowerCarbonIntensity, PowerPrice, GasPrice


router = APIRouter(tags=["Time-Series"])


@router.get("/timeseries/power-carbon-intensity")
def get_power_carbon_intensity(
    start_date: datetime.datetime, 
    end_date: datetime.datetime
) -> list[PowerCarbonIntensity]:
    return [PowerCarbonIntensity(
        start_time=datetime.datetime(2024, 1, 1, 12, 30),
        value=123.45
    )]

@router.get("/timeseries/power-price")
def get_power_price(
    start_date: datetime.datetime, 
    end_date: datetime.datetime
) -> list[PowerPrice]:
    return [PowerPrice(
        start_time=datetime.datetime(2024, 1, 1, 12, 30),
        value=123.45
    )]

@router.get("/timeseries/gas-price")
def get_gas_price(
    start_date: datetime.datetime, 
    end_date: datetime.datetime
) -> list[GasPrice]:
    return [GasPrice(
        start_time=datetime.datetime(2024, 1, 1, 12, 30),
        value=123.45
    )]
