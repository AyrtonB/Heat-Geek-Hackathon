import datetime
from enum import Enum

from pydantic import BaseModel


class DataProviderEnum(str, Enum):
    APXMIDP = 'APXMIDP'
    N2EXMIDP = 'N2EXMIDP'


class MarketIndex(BaseModel):
    startTime: datetime.datetime
    dataProvider: DataProviderEnum
    settlementDate: datetime.datetime
    settlementPeriod: int
    price: float
    volume: float
