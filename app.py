import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="AQI Forecaster",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Views
from views import home, realtime, forecasting, india_aqi, quantum, anomaly, heatmap

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
    # Clear param so refresh doesn't stick
    # st.query_params.clear() # Optional, but keeps URL clean. Let's keep it for now.

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
