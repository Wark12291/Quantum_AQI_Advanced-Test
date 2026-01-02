import streamlit as st

def show_precautions():
    st.markdown("<h1 class='neon-title'>Precautions & Prevention</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>Indoor Measures</h4>
<p>Since we spend most of our time indoors, maintaining good indoor air quality is crucial.</p>
<ul>
<li><strong>Air Purifiers:</strong> Use HEPA (High Efficiency Particulate Air) filters to remove fine particles. Ensure the unit is rated for the room size.</li>
<li><strong>Ventilation:</strong> On days with good AQI, open windows to circulate fresh air. Keep them closed during high pollution spikes.</li>
<li><strong>Indoor Plants:</strong> Plants like Snake Plant, Spider Plant, and Aloe Vera act as natural air purifiers (though their effect is mild compared to mechanical purifiers).</li>
<li><strong>Avoid Indoor Sources:</strong> Minimize use of incense sticks, candles, and frying food without exhaust fans.</li>
<li><strong>Regular Cleaning:</strong> Wet mop floors and use a vacuum with a HEPA filter to reduce dust.</li>
</ul>
</div>
<h3 class="section-header">Outdoor Precautions</h3>
<div class="neon-box">
<ul>
<li><strong>Check AQI Daily:</strong> Make it a habit to check the AQI forecast before planning outdoor activities.</li>
<li><strong>Wear Masks:</strong> When AQI is 'Unhealthy' or worse, use N95 or N99 masks. Cloth masks offer minimal protection against PM2.5.</li>
<li><strong>Limit Excercise:</strong> Avoid strenuous outdoor exercise when pollution levels are high. You breathe deeper and faster during exercise, inhaling more pollutants.</li>
<li><strong>Time Your Outings:</strong> Pollution is often highest in the morning and evening rush hours. Mid-day might be clearer in some seasons.</li>
</ul>
</div>
<h3 class="section-header">Travel Safety</h3>
<div class="neon-box">
<ul>
<li><strong>Recirculate Air:</strong> When driving in heavy traffic, set your car's ventilation to 'recirculate' mode to avoid drawing in exhaust fumes.</li>
<li><strong>Change Cabin Filters:</strong> Ensure your car's cabin air filter is high quality and changed regularly.</li>
<li><strong>Avoid Hotspots:</strong> Walk or cycle on side streets away from main roads where vehicle emissions are concentrated.</li>
</ul>
</div>
<div class="neon-box">
<h4>Natural Remedies & Diet</h4>
<p>A healthy diet can boost your body's resilience against pollution.</p>
<ul>
<li><strong>Antioxidants:</strong> Vitamin C (citrus fruits) and Vitamin E (nuts, seeds) help combat oxidative stress caused by pollution.</li>
<li><strong>Omega-3 Fatty Acids:</strong> Found in fish, flaxseeds, and walnuts, these reduce inflammation.</li>
<li><strong>Hydration:</strong> Drink plenty of water to help your body flush out toxins.</li>
<li><strong>Jaggery (Gur):</strong> Traditional wisdom suggests jaggery may help clear the respiratory tract.</li>
</ul>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
