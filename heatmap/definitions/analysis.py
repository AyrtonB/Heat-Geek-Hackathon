from pydantic import BaseModel
from typing import List



class KeyValue(BaseModel):
    key: str
    value: str


class OpexEstimate(BaseModel):
    annual: List[KeyValue]
