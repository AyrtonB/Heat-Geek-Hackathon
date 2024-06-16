# Heat-Geek-Hackathon

<br>

### Setup

* Install poetry - [link](https://python-poetry.org/docs/#installation)
* Run `poetry install`
* Ensure you have been sent the `.env`, `temperature_2020_2032.csv` and `heatmap.db` files
* Ensure you have a directory called `static` under `heatmap/api/`
* Run `poetry run python main.py`

<br>

#### Deployment

* API: `gcloud run deploy --quiet https://heat-geek-hackathon-4zuwmrh3fq-nw.a.run.app/analysis/opex-estimate?scops=2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.` => https://heat-geek-hackathon-4zuwmrh3fq-nw.a.run.app/docs
* Frontend: `cd frontend && gcloud run deploy --quiet https://frontend-4zuwmrh3fq-nw.a.run.app/` => https://frontend-4zuwmrh3fq-nw.a.run.app/
* Streamlit: `cd streamlit && gcloud run deploy --quiet` => https://streamlit-4zuwmrh3fq-nw.a.run.app/


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
