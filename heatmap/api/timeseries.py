import datetime
import os

from dotenv import load_dotenv
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

from heatmap.db import get_records_within_dates
from heatmap.definitions.timeseries import GasPrice, PowerCarbonIntensity, PowerPrice

router = APIRouter(tags=["Time-Series"])


load_dotenv()
DB_CONN_STR = os.environ['DB_CONN_STR']

engine = create_engine(url=DB_CONN_STR)
bound_sessionmaker = sessionmaker(engine)


@router.get("/power-carbon-intensity")
def get_power_carbon_intensity(
    start_date: datetime.datetime, end_date: datetime.datetime
) -> list[PowerCarbonIntensity]:
    with bound_sessionmaker() as session:
        return get_records_within_dates(session, start_date, end_date)


@router.get("/power-price")
def get_power_price(start_date: datetime.datetime, end_date: datetime.datetime) -> list[PowerPrice]:
    return [PowerPrice(start_time=datetime.datetime(2024, 1, 1, 12, 30), value=123.45)]


@router.get("/gas-price")
def get_gas_price(start_date: datetime.datetime, end_date: datetime.datetime) -> list[GasPrice]:
    return [GasPrice(start_time=datetime.datetime(2024, 1, 1, 12, 30), value=123.45)]
