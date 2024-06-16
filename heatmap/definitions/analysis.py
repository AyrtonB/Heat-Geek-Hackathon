from pydantic import BaseModel
from typing import List



class KeyValue(BaseModel):
    key: str
    value: str


class OpexEstimate(BaseModel):
    min_scops: float
    annual: List[KeyValue]
