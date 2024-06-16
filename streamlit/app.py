#%%
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

#%%
# Enable wide mode
st.set_page_config(layout="wide")

st.title("Good COP, Bad COP")

params = {
    "start_date" : "2024-01-15T19:08:28.025Z",
    "end_date" : "2024-01-15T19:08:28.025Z"
}
@st.cache_data()
def load_data():
    temp_data = pd.read_csv("data/Heat_pump_energy_usage.csv")
    temp_data.rename(columns={'timestamp': 'Time'}, inplace=True)

    return temp_data

temp_data = load_data()

min_cop = st.slider("Min COP", value=1.5, max_value=5.0)
max_cop = st.slider("Max COP", value=3.0, max_value=5.0)

initial_heatpumps = 100000
final_heatpumps = st.slider("Final Heatpumps ", 1000000, 5000000, step=1000000)


# def load_temperature_s(temperature_fp):
#     s_temperature = pd.read_csv(temperature_fp).set_index('timestamp')['temperature']
#     s_temperature.index = pd.to_datetime(s_temperature.index)

#     full_dt_idx = pd.date_range(start=s_temperature.index[0], end=s_temperature.index[-1], freq='h')
#     assert s_temperature.reindex(full_dt_idx).isnull().sum() == 0, 'There are missing values in the temperature data.'

#     return s_temperature

# def calculate_heating_load(s_temperature: pd.Series, 
#                            heating_on_temperature: float, 
#                            avg_heating_use_kwh: float) -> pd.Series:
#     s_temperature_diff = heating_on_temperature - s_temperature
#     s_temperature_diff.loc[s_temperature > heating_on_temperature] = 0

#     n_years = (s_temperature_diff.index[-1]-s_temperature_diff.index[0]).total_seconds() / (365 * 24 * 3600)

#     total_heating_over_period = n_years * avg_heating_use_kwh
#     heating_load_per_temp_diff = total_heating_over_period / s_temperature_diff.sum()
#     return s_temperature_diff.multiply(heating_load_per_temp_diff)

def linear_cop(temp, min_temp=-5, max_temp=20, min_cop=3.5, max_cop=7.5):
    slope = (max_cop - min_cop) / (max_temp - min_temp)
    intercept = min_cop - slope * min_temp

    if temp <= min_temp:
        return min_cop
    elif temp >= max_temp:
        return max_cop
    else:
        return slope * temp + intercept
    
def interpolate_heatpumps(df, 
                          start_date='2020-01-01', 
                          end_date='2032-12-31', 
                          initial_heatpumps=100000, 
                          final_heatpumps=300000, 
                          speed_factor=2.5):
    """
    Interpolates the number of heat pumps installed between a start date and an end date as whole numbers,
    with the speed of installations increasing towards the end of the period.
    
    Args:
        df (pandas.DataFrame): The input DataFrame containing a DatetimeIndex.
        start_date (str): The start date for interpolation in the format 'YYYY-MM-DD'.
        end_date (str): The end date for interpolation in the format 'YYYY-MM-DD'.
        initial_heatpumps (int): The initial number of heat pumps installed at the start date.
        final_heatpumps (int): The final number of heat pumps installed at the end date.
        speed_factor (float, optional): A factor controlling the speed of installations. Higher values result in more
                                         installations towards the end of the period. Default is 1.0.
    
    Returns:
        pandas.DataFrame: The input DataFrame with a new column 'heatpumps_installed' containing the interpolated values.
    """
    # Convert start and end dates to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Create a new column 'heatpumps_installed' initialized with NaN values
    df['heatpumps_installed'] = np.nan
    
    # Calculate the total number of days between start and end dates
    total_days = (end_date - start_date).days
    
    # Calculate the total number of heat pumps to be installed
    total_heatpumps = final_heatpumps - initial_heatpumps
    
    # Generate a sequence of numbers from 0 to 1 with a length equal to the total number of days
    time_factor = np.linspace(0, 1, total_days + 1) ** speed_factor
    
    # Calculate the cumulative number of heat pumps installed for each day
    cumulative_heatpumps = initial_heatpumps + (total_heatpumps * time_factor).astype(int)
    
    # Assign the cumulative number of heat pumps to each date in the DataFrame
    for idx, date in enumerate(pd.date_range(start_date, end_date)):
        df.loc[date, 'heatpumps_installed'] = cumulative_heatpumps[idx]
    
    # Fill the remaining dates before the start date with the initial number of heat pumps
    df.loc[:start_date, 'heatpumps_installed'] = initial_heatpumps
    
    # Fill the remaining dates after the end date with the final number of heat pumps
    df.loc[end_date:, 'heatpumps_installed'] = final_heatpumps
    
    return df

interpolate_heatpumps(df=temp_data, final_heatpumps=final_heatpumps)

temp_data['COP'] = temp_data.apply(lambda x: linear_cop(x['Temp'], min_cop=min_cop, max_cop=max_cop), axis=1)

temp_data['PowerSaved'] = temp_data['hourly_heating_load_hour_kWh'] * temp_data['heatpumps_installed']


# power_carbon_intense = requests.get("http://10.13.22.45:8000/timeseries/power-carbon-intensity", params=params)
print("creating graph")
 # Create an interactive line chart
chart = alt.Chart(temp_data).mark_line().encode(
    x=alt.X('Time:T', title='Time', axis=alt.Axis(format='%Y %b')),   # The ':T' tells Altair that the data is temporal
    y=alt.Y('PowerSaved:Q', title='Power Saved'),  # The ':Q' tells Altair that the data is quantitative
    # color=alt.Color('PostcodeDistrict:N', legend=alt.Legend(title="Postcode District")),  # Different line for each postcode_district
    # tooltip=['PostcodeDistrict:N', 'Year:T', 'AvgPrice:Q', 'NumTransactions:Q']  # Tooltips for interactivity
).properties(
    title = 'Power Saved'
).interactive()

# Display the chart in the Streamlit app
st.altair_chart(chart, use_container_width=True)



# %%
