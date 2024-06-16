import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from heatmap.api import analysis, timeseries

# Inputs
load_dotenv()
static_dir = os.environ["STATIC_DIR"]


# Initialisation
app = FastAPI(
    title="Heat Geek Hackathon", description='Yo yo yo, this is the API for the Heat Rash team.', version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(analysis.router, prefix="/analysis")
app.include_router(timeseries.router, prefix="/timeseries")
