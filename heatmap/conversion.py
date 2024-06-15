from heatmap.definitions.ng_carbon_intensity import (
    Response as NgCarbonIntensityResponse,
)
from heatmap.definitions.timeseries import PowerCarbonIntensity


def ng_to_core_power_carbon_intensity(
    ng_carbon_intensity_response: NgCarbonIntensityResponse,
) -> list[PowerCarbonIntensity]:
    return [
        PowerCarbonIntensity(start_time=data_record.from_, end_time=data_record.to, value=data_record.intensity.actual)
        for data_record in ng_carbon_intensity_response.data
        if data_record.intensity.actual is not None
    ]
