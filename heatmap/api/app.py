import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from heatmap.api import timeseries


# Inputs
load_dotenv()
static_dir = os.environ["STATIC_DIR"]


# Initialisation
app = FastAPI(
    title="Heat Geek Hackathon",
    description='Yo yo yo, this is the API for Heat Geek Hackathon.',
    version="0.1.0"
)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(timeseries.router)
