#%%
import streamlit as st
import requests
import altair as alt
import pandas as pd

#%%
# Enable wide mode
st.set_page_config(layout="wide")

st.title("Heat Pump Policy Impacts")

params = {
    "start_date" : "2024-01-15T19:08:28.025Z",
    "end_date" : "2024-01-15T19:08:28.025Z"
}
@st.cache_data()
def load_data():
    temp_data = pd.read_csv("data/temperature_2020_2032_with_tempdiff.csv")
    temp_data.rename(columns={'timestamp': 'Time'}, inplace=True)

    return temp_data

temp_data = load_data()

# power_carbon_intense = requests.get("http://10.13.22.45:8000/timeseries/power-carbon-intensity", params=params)

 # Create an interactive line chart
chart = alt.Chart(temp_data).mark_line().encode(
    x='Time:T',  # The ':T' tells Altair that the data is temporal
    y=alt.Y('Temp_diff:Q', title='Temperature Differential'),  # The ':Q' tells Altair that the data is quantitative
    # color=alt.Color('PostcodeDistrict:N', legend=alt.Legend(title="Postcode District")),  # Different line for each postcode_district
    tooltip=['PostcodeDistrict:N', 'Year:T', 'AvgPrice:Q', 'NumTransactions:Q']  # Tooltips for interactivity
).properties(
    title = 'Change of Temperature over time'
).interactive()

# Display the chart in the Streamlit app
st.altair_chart(chart, use_container_width=True)

st.slider("Min COP", value=1.5, max_value=5.0)
st.slider("Max COP", value=3.0, max_value=5.0)
st.slider("", value=3.0, max_value=5.0)

# %%
