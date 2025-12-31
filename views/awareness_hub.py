import streamlit as st

def show_awareness_hub():
    """Main Awareness Hub Dashboard with 8 clickable cards"""
    
    # Header Section
    st.markdown("""
<div class='awareness-hub-header'>
<h1 class='awareness-hub-title'>📚 AQI Awareness & Safety Hub</h1>
<p class='awareness-hub-subtitle'>A complete environmental knowledge center with scientific insights</p>
</div>
""", unsafe_allow_html=True)
    
    # Back to Home Button
    st.markdown("""
<a href="?nav=home" target="_self">
<button class="awareness-back-btn">⬅ Back to Home</button>
</a>
<br><br>
""", unsafe_allow_html=True)
    
    # 8 Awareness Cards in 4x2 Grid
    st.markdown("""
<div class='awareness-card-grid'>
<a href="?nav=understanding_aqi" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>📊 Understanding AQI</h3>
<p>Learn about Air Quality Index fundamentals</p>
</div>
</a>
<a href="?nav=health_impact" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>❤️ Health Impact</h3>
<p>How pollution affects your body</p>
</div>
</a>
<a href="?nav=precautions" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>🛡️ Precautions</h3>
<p>Protect yourself from air pollution</p>
</div>
</a>
<a href="?nav=pollution_control" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>🌱 Pollution Control</h3>
<p>Actions to reduce air pollution</p>
</div>
</a>
<a href="?nav=aqi_devices" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>📡 AQI Devices & IoT</h3>
<p>Technology for air quality monitoring</p>
</div>
</a>
<a href="?nav=quantum_insights" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>⚛️ Quantum Insights</h3>
<p>Quantum computing in pollution analysis</p>
</div>
</a>
<a href="?nav=diseases_caused" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>🏥 Diseases Caused</h3>
<p>Health conditions from air pollution</p>
</div>
</a>
<a href="?nav=safety_measures" target="_self" style="text-decoration: none;">
<div class='awareness-neon-card'>
<h3>🚨 Safety Measures</h3>
<p>Emergency protocols and daily safety</p>
</div>
</a>
</div>
""", unsafe_allow_html=True)
