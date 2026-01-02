import streamlit as st

def show_aqi_devices():
    st.markdown("<h1 class='neon-title'>📡 AQI Devices & IoT Monitoring</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>🏠 Consumer AQI Monitors</h4>
<p>Affordable devices for home use to track indoor air quality.</p>
<ul>
<li><strong>Laser Scattering Sensors:</strong> Most common sensor type (e.g., Plantower sensors) for detecting PM2.5.</li>
<li><strong>Features to Look For:</strong> Real-time display, historical logging app, PM2.5 + CO2 detection, battery life.</li>
<li><strong>Why you need one:</strong> You can't improve what you don't measure. Knowing when indoor air is bad prompts you to turn on filters.</li>
</ul>
</div>
<h3 class="section-header">🌐 IoT Sensor Networks</h3>
<div class="neon-box">
<p>The future of monitoring is hyper-local data through Internet of Things (IoT).</p>
<ul>
<li><strong>Low-Cost Sensors:</strong> Deploying thousands of cheap sensors across a city instead of a few expensive stations.</li>
<li><strong>Data Fusion:</strong> Combining sensor data with satellite imagery and traffic data for precision mapping.</li>
<li><strong>Smart City Integration:</strong> Traffic lights that adjust timing based on local pollution levels to reduce idling.</li>
</ul>
</div>
<h3 class="section-header">🛰️ Satellite Monitoring</h3>
<div class="neon-box">
<p>Satellites provide a bird's-eye view of pollution movement across continents.</p>
<ul>
<li><strong>Aerosol Optical Depth (AOD):</strong> Satellites measure how much sunlight is blocked by particles in the atmosphere.</li>
<li><strong>Tracking Sources:</strong> identifying forest fires, dust storms, and industrial hotspots from space.</li>
<li><strong>NASA & ESA:</strong> Satellites like Sentinel-5P provide high-resolution data on gases like NO2 and Ozone.</li>
</ul>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
