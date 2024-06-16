import pandas as pd


def load_temperature_s(temperature_fp):
    s_temperature = pd.read_csv(temperature_fp).set_index('timestamp')['temperature']
    s_temperature.index = pd.to_datetime(s_temperature.index)

    full_dt_idx = pd.date_range(start=s_temperature.index[0], end=s_temperature.index[-1], freq='h')
    assert s_temperature.reindex(full_dt_idx).isnull().sum() == 0, 'There are missing values in the temperature data.'

    return s_temperature

def calculate_heating_load(s_temperature: pd.Series, heating_on_temperature: float, annual_heat_kwh_consumption: float) -> pd.Series:
    heating_on_temperature = float(heating_on_temperature)
    s_temperature_diff = heating_on_temperature - s_temperature
    s_temperature_diff.loc[s_temperature > heating_on_temperature] = 0

    n_years = (s_temperature_diff.index[-1]-s_temperature_diff.index[0]).total_seconds() / (365 * 24 * 3600)

    total_heating_over_period = n_years * annual_heat_kwh_consumption
    heating_load_per_temp_diff = total_heating_over_period / s_temperature_diff.sum()
    return s_temperature_diff.multiply(heating_load_per_temp_diff)

def linear_cop(temp, min_temp=-5, max_temp=20, min_cop=3.5, max_cop=7.5):
    slope = (max_cop - min_cop) / (max_temp - min_temp)
    intercept = min_cop - slope * min_temp

    if temp <= min_temp:
        return min_cop
    elif temp >= max_temp:
        return max_cop
    else:
        return slope * temp + intercept
    
def get_opex_estimate_ts_df(
    s_temperature: pd.Series,
    min_cop: str = '3.5',
    annual_heat_kwh_consumption: float = 12000, 
    heating_on_temperature = 17.0,
    min_temp = -5,
    max_temp = 20,
    max_cop = 7.5,
    n_households: int = 1
) -> pd.DataFrame:
    s_heating_load_kwh = calculate_heating_load(s_temperature, heating_on_temperature, annual_heat_kwh_consumption*n_households)
    s_cop = s_temperature.apply(linear_cop, args=(min_temp, max_temp, min_cop, max_cop))
    s_elec_load_kwh = s_heating_load_kwh.divide(s_cop)

    return pd.concat([
        s_temperature,
        s_heating_load_kwh.rename('heating_load_kwh'),
        s_cop.rename('cop'),
        s_elec_load_kwh.rename('elec_load_kwh'),
    ], axis=1)
