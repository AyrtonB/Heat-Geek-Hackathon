import datetime

from heatmap.definitions.ng_carbon_intensity import (
    Response as NgCarbonIntensityResponse,
)
from heatmap.definitions.elexon import MarketIndex
from heatmap.definitions.timeseries import PowerCarbonIntensity, PowerPrice


def ng_to_core__power_carbon_intensity(
    ng_carbon_intensity_response: NgCarbonIntensityResponse,
) -> list[PowerCarbonIntensity]:
    return [
        PowerCarbonIntensity(start_time=data_record.from_, end_time=data_record.to, value=data_record.intensity.actual)
        for data_record in ng_carbon_intensity_response.data
        if data_record.intensity.actual is not None
    ]

def elexon_to_core__power_market_index(
    market_index_records: list[MarketIndex],
) -> list[PowerPrice]:
    return [
        PowerPrice(start_time=mir.startTime, end_time=mir.startTime+datetime.timedelta(minutes=30), value=mir.price)
        for mir in market_index_records
    ]
