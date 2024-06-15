import datetime

from sqlmodel import Field, SQLModel


class PointInTimeRecord(SQLModel):
    start_time: datetime.datetime
    end_time: datetime.datetime
    value: float


class PowerCarbonIntensity(PointInTimeRecord, table=True):
    __tablename__ = "power_carbon_intensity"
    start_time: datetime.datetime = Field(primary_key=True)


class PowerPrice(PointInTimeRecord, table=True):
    __tablename__ = "power_price_gbp_per_mwh"
    start_time: datetime.datetime = Field(primary_key=True)


class GasPrice(PointInTimeRecord, table=True):
    __tablename__ = "gas_price_gbp_per_mwh"
    start_time: datetime.datetime = Field(primary_key=True)
