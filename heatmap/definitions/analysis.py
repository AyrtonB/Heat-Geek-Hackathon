import datetime
from typing import Any

from pydantic import BaseModel


class KeyValue(BaseModel):
    key: str
    value: str


class HeatPumpTimeSeriesRecord(BaseModel):
    timestamp: datetime.datetime
    temperature: float
    heating_load_kwh: float
    cop: float
    elec_load_kwh: float


class OpexEstimate(BaseModel):
    min_scops: float
    annual: list[KeyValue]
    timeseries: list[HeatPumpTimeSeriesRecord]
