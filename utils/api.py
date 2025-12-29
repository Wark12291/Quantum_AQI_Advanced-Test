import requests
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import config

@st.cache_data(ttl=3600)
def fetch_aqi(city):
    """
    Fetch real-time AQI data for a given city using WAQI API.
    """
    url = f"{config.BASE_URL}/{city}/?token={config.API_TOKEN}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            return data['data']
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

@st.cache_data(ttl=3600)
def fetch_all_cities_aqi():
    """
    Fetch AQI for all configured cities.
    Returns a DataFrame.
    """
    results = []
    for city in config.AQI_CITIES:
        data = fetch_aqi(city)
        if data:
            aqi = data.get('aqi')
            # WaQI sometimes returns '-' for aqi
            if str(aqi).isdigit():
                 results.append({
                    "City": city.title(),
                    "AQI": int(aqi),
                    "Dominant Pollutant": data.get('dominentpol', 'N/A'),
                    "Last Update": data.get('time', {}).get('s', 'N/A')
                })
    
    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values(by="AQI", ascending=False)
    return df

def get_historical_data_simulated(days=90):
    """
    Simulate historical data for demonstration since the free API 
    doesn't always provide easy historical access without limits.
    """
    # Create base dates
    base_dates = [datetime.today() - timedelta(days=x) for x in range(days)]
    
    # Add random time offsets to each day for realism
    dates = []
    for d in base_dates:
        # Give each day a unique time (e.g. between 00:00 and 23:59)
        h = np.random.randint(0, 24)
        m = np.random.randint(0, 60)
        s = np.random.randint(0, 60)
        dates.append(d.replace(hour=h, minute=m, second=s))
    
    dates.sort() # Ensure chronological order
    
    # Simulate some seasonal trend + noise
    base_aqi = 100
    values = []
    for i, _ in enumerate(dates):
        # Trend: higher in winter (end of year), lower in summer
        seasonal = 50 * np.sin(2 * np.pi * i / 365) 
        noise = np.random.normal(0, 15)
        aqi = max(20, base_aqi + seasonal + noise)
        values.append(int(aqi))
        
    df = pd.DataFrame({"Date": dates, "AQI": values})
    df.set_index("Date", inplace=True)
    return df
