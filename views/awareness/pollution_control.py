import streamlit as st

def show_pollution_control():
    st.markdown("<h1 class='neon-title'>🌱 Pollution Control Actions</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>👤 Individual Actions</h4>
<p>Every small step counts when millions participate.</p>
<ul>
<li><strong>Reduce Vehicle Use:</strong> Carpool, use public transport, cycle, or walk whenever possible.</li>
<li><strong>Save Energy:</strong> Turn off lights/appliances when not in use. Energy generation is a major source of pollution.</li>
<li><strong>Sustainable Disposal:</strong> Avoid burning trash, leaves, or plastic. Separate waste for recycling.</li>
<li><strong>Plant Trees:</strong> Trees are natural air filters. Participate in local plantation drives.</li>
<li><strong>Solar Power:</strong> Switch to solar energy for home if feasible.</li>
</ul>
</div>
<h3 class="section-header">🏘️ Community & Government Actions</h3>
<div class="neon-box">
<ul>
<li><strong>Green Transport:</strong> Investment in electric buses and expanding metro networks.</li>
<li><strong>Construction Dust Control:</strong> Strict regulations on covering construction sites and sprinkling water to settle dust.</li>
<li><strong>Industrial Regulation:</strong> Mandatory installation of scrubbers and filters in factory chimneys (Particulate Control Devices).</li>
<li><strong>Crop Residue Management:</strong> Subsidizing machinery for farmers to manage stubble instead of burning it.</li>
</ul>
</div>
<h3 class="section-header">🚀 Future Technologies</h3>
<div class="neon-box">
<h4>Smog Towers & Air Cleaning</h4>
<p>Large-scale air purifiers installed in cities to filter air in a localized 1km radius.</p>
<h4>Cloud Seeding</h4>
<p>Artificial rain generation to wash away suspended pollutants during severe smog episodes.</p>
<h4>Bio-Filters</h4>
<p>Using algae and moss walls in urban furniture to absorb CO2 and particulate matter.</p>
</div>
<br>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
