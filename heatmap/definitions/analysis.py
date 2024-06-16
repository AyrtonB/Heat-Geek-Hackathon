from typing import List

from pydantic import BaseModel


class KeyValue(BaseModel):
    key: str
    value: str


class OpexEstimate(BaseModel):
    min_scops: float
    annual: List[KeyValue]
