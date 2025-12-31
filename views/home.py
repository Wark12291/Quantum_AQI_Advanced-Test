import streamlit as st
from streamlit_option_menu import option_menu

def show_home():
    st.markdown("""
<style>
@keyframes neon-breathe {
0%, 100% { 
text-shadow: 0 0 10px #00f3ff, 0 0 20px #00f3ff;
box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
}
50% { 
text-shadow: 0 0 15px #00f3ff, 0 0 30px #00f3ff, 0 0 40px #00f3ff;
box-shadow: 0 0 25px rgba(0, 243, 255, 0.4);
}
}
.premium-header {
text-align: center;
margin-bottom: 40px;
}
.main-title {
font-size: 3.2rem !important;
font-weight: 800 !important;
color: #ffffff !important;
text-shadow: 0 0 10px #00f3ff, 0 0 20px #00f3ff;
letter-spacing: 2px;
margin-bottom: 25px !important;
}
.sub-header-container {
display: inline-block;
padding: 15px 40px;
background: rgba(18, 24, 38, 0.6);
backdrop-filter: blur(12px);
-webkit-backdrop-filter: blur(12px);
border: 1px solid rgba(0, 243, 255, 0.3);
border-radius: 15px;
box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
animation: neon-breathe 4s infinite ease-in-out;
transition: 0.3s;
}
.sub-header-text {
color: #00ff88 !important;
margin: 0 !important;
font-size: 1.4rem !important;
font-weight: 500 !important;
letter-spacing: 1px;
text-transform: uppercase;
}
</style>
<div class='premium-header'>
<h1 class='main-title'>Welcome to AQI Forecaster</h1>
<div class='sub-header-container'>
<h3 class='sub-header-text'>Advanced AI & Quantum Powered Air Quality Analytics</h3>
</div>
</div>
""", unsafe_allow_html=True)

    # Grid Layout for Features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
<a href="?nav=realtime" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>🌍 Real-Time AQI</h3>
<p>Live pollution data monitoring for any city.</p>
</div>
</a>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<a href="?nav=forecasting" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>📈 AQI Forecasting</h3>
<p>Predict future AQI with ARIMA & LSTM models.</p>
</div>
</a>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<a href="?nav=india_aqi" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>India AQI</h3>
<p>Top 20 major cities analysis & comparison.</p>
</div>
</a>
""", unsafe_allow_html=True)

    st.markdown("---")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
<a href="?nav=quantum" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>⚛️ Quantum Module</h3>
<p>Quantum noise simulation using Qiskit.</p>
</div>
</a>
""", unsafe_allow_html=True)

    with col5:
        st.markdown("""
<a href="?nav=anomaly" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>⚠️ Anomaly Detection</h3>
<p>Spot sudden spikes in pollution levels.</p>
</div>
</a>
""", unsafe_allow_html=True)

    with col6:
        st.markdown("""
<a href="?nav=heatmap" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>🗺️ Heatmap</h3>
<p>Interactive geospatial pollution map.</p>
</div>
</a>
""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Awareness Hub Single Card Link (Centered below other cards)
    col_spacer_left, col_center, col_spacer_right = st.columns([1, 1, 1])

    with col_center:
        st.markdown("""
<a href="?nav=awareness_hub" target="_self" style="text-decoration: none;">
<div class="neon-card">
<h3>📚 AQI Awareness & Safety Hub</h3>
<p>A complete environmental knowledge center with scientific insights. Click to explore.</p>
</div>
</a>
""", unsafe_allow_html=True)
