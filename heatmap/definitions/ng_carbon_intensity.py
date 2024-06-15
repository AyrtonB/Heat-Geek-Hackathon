import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Intensity(BaseModel):
    forecast: float
    actual: Optional[float]
    index: str


class DataRecord(BaseModel):
    from_: datetime.datetime = Field(alias="from")
    to: datetime.datetime
    intensity: Intensity


class Response(BaseModel):
    data: list[DataRecord]
