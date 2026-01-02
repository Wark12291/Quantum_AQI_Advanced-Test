import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="AQI Forecaster",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)



# Load Views - Main
from views import home, realtime, forecasting, india_aqi, quantum, anomaly, heatmap

# Load Views - Awareness Hub Subpages
from views.awareness import (
    understanding_aqi,
    health_impact,
    precautions,
    pollution_control,
    aqi_devices,
    quantum_insights,
    diseases_caused,
    safety_measures
)

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# Session State for Navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Handle Query Params for Navigation
params = st.query_params
if "nav" in params:
    st.session_state['page'] = params["nav"]

# Navigation Logic
if st.session_state['page'] == 'home':
    home.show_home()
elif st.session_state['page'] == 'realtime':
    realtime.show_realtime()
elif st.session_state['page'] == 'forecasting':
    forecasting.show_forecasting()
elif st.session_state['page'] == 'india_aqi':
    india_aqi.show_india_aqi()
elif st.session_state['page'] == 'quantum':
    quantum.show_quantum()
elif st.session_state['page'] == 'anomaly':
    anomaly.show_anomaly()
elif st.session_state['page'] == 'heatmap':
    heatmap.show_heatmap()

# Awareness Hub Main Dashboard
elif st.session_state['page'] == 'awareness_hub':
    from views import awareness_hub
    awareness_hub.show_awareness_hub()

# Awareness Hub Sub-Pages
elif st.session_state['page'] == 'understanding_aqi':
    understanding_aqi.show_understanding_aqi()
elif st.session_state['page'] == 'health_impact':
    health_impact.show_health_impact()
elif st.session_state['page'] == 'precautions':
    precautions.show_precautions()
elif st.session_state['page'] == 'pollution_control':
    pollution_control.show_pollution_control()
elif st.session_state['page'] == 'aqi_devices':
    aqi_devices.show_aqi_devices()
elif st.session_state['page'] == 'quantum_insights':
    quantum_insights.show_quantum_insights()
elif st.session_state['page'] == 'diseases_caused':
    diseases_caused.show_diseases_caused()
elif st.session_state['page'] == 'safety_measures':
    safety_measures.show_safety_measures()
