import streamlit as st
import folium
from streamlit_folium import st_folium
import utils.api as api
from folium.plugins import HeatMap

def show_heatmap():
    st.markdown("## 🗺️ AQI Geospatial Heatmap")
    
    st.markdown("""
    <a href="?nav=home" target="_self">
        <button style="
            background: linear-gradient(45deg, #00f3ff, #bd00ff);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(189, 0, 255, 0.5);
        ">⬅ Back to Home</button>
    </a>
    <br><br>
    """, unsafe_allow_html=True)
        
    df = api.fetch_all_cities_aqi()
    
    if df.empty:
        st.error("No data available for heatmap.")
        return

    # Coordinates for major cities (Hardcoded for demo speed, ideally from a persistent Geo DB)
    # Using a simple dictionary for the Top 20 listed in config
    city_coords = {
        "Delhi": [28.7041, 77.1025], "Mumbai": [19.0760, 72.8777], "Kolkata": [22.5726, 88.3639],
        "Chennai": [13.0827, 80.2707], "Bangalore": [12.9716, 77.5946], "Hyderabad": [17.3850, 78.4867],
        "Pune": [18.5204, 73.8567], "Ahmedabad": [23.0225, 72.5714], "Lucknow": [26.8467, 80.9462],
        "Jaipur": [26.9124, 75.7873], "Patna": [25.5941, 85.1376], "Kanpur": [26.4499, 80.3319],
        "Visakhapatnam": [17.6868, 83.2185], "Chandigarh": [30.7333, 76.7794], "Bhopal": [23.2599, 77.4126],
        "Indore": [22.7196, 75.8577], "Nagpur": [21.1458, 79.0882], "Surat": [21.1702, 72.8311],
        "Coimbatore": [11.0168, 76.9558], "Tirupati": [13.6288, 79.4192],
        "Vijayawada": [16.5062, 80.6480], "Varanasi": [25.3176, 82.9739], "Dehradun": [30.3165, 78.0322]
    }
    
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles='CartoDB dark_matter')
    
    heat_data = []
    
    for index, row in df.iterrows():
        city_name = row['City']
        aqi = row['AQI']
        coords = city_coords.get(city_name)
        
        if coords:
            # Color marker based on AQI
            color = 'green'
            if aqi > 50: color = 'yellow'
            if aqi > 100: color = 'orange'
            if aqi > 150: color = 'red'
            if aqi > 200: color = 'purple'
            if aqi > 300: color = 'darkred'
            
            folium.Marker(
                location=coords,
                popup=f"<b>{city_name}</b><br>AQI: {aqi}",
                icon=folium.Icon(color=color, icon='cloud')
            ).add_to(m)
            
            heat_data.append([coords[0], coords[1], aqi])
            
    HeatMap(heat_data).add_to(m)
    
    st_folium(m, use_container_width=True, height=550)
    
    st.info("Dark Mode Map enabled for Neon Theme consistency.")
