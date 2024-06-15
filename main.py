import os

import uvicorn
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

from heatmap.definitions.timeseries import PowerCarbonIntensity, PowerPrice, GasPrice


load_dotenv()
HOST = os.environ["HOST"]
DB_CONN_STR = os.environ['DB_CONN_STR']


if __name__ == '__main__':
    engine = create_engine(url=DB_CONN_STR)
    SQLModel.metadata.create_all(engine, tables=[
        PowerCarbonIntensity.__table__, 
        PowerPrice.__table__, 
        GasPrice.__table__
    ])

    uvicorn.run("heatmap.api.app:app", host=HOST, port=8000, reload=True)
