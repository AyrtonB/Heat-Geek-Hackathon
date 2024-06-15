# Heat-Geek-Hackathon

<br>

### Setup

* Install poetry - [link](https://python-poetry.org/docs/#installation)
* Run `poetry install`
* Ensure you have been sent the `.env` and `heatmap.db` files
* Run `poetry run python main.py`

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
