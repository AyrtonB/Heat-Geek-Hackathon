# Heat-Geek-Hackathon

<br>

### Setup

* Install poetry - [link](https://python-poetry.org/docs/#installation)
* Run `poetry install`
* Ensure you have been sent the `.env` and `heatmap.db` files
* Ensure you have a directory called `static` under `heatmap/api/`
* Run `poetry run python main.py`

<br>


#### Deployment
* API: `gcloud run deploy`
* Frontend: `cd frontend && gcloud run deploy`
* Streamlit: `cd streamlit && gcloud run deploy`


<br>

### Open Qs

* Point-in-time v historical/long-term
* Bottom-up v Top-down

<br>

### Data Inputs

Time-series
* Fuel Mix
  * Elexon - FUELHH/FUELINST (30min v 5 min
* Power Prices
  * Electric Insights - historical
  * Elexon/EPEX - going forward
* Gas Prices
  * Statista - (monthly) historical
  * ICE - going forward
* AGSI
  * Gas import/export
* Carbon Intensity
  * Dukes avg gCO2/kWh for different fuel
  * ETS/Elexon - Bottom-up power plant level estimates - https://osuked.github.io/Power-Station-Dictionary/datasets/carbon-intensity.html
* Temperature
  * Elexon - https://bmrs.elexon.co.uk/temperature  
   
<br>

Spatial Inputs
* TODO

<br>

### 
