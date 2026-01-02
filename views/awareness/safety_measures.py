import streamlit as st

def show_safety_measures():
    st.markdown("<h1 class='neon-title'>Emergency Safety Measures</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>Immediate Actions during High AQI (300+)</h4>
<ol>
<li><strong>Stay Indoors:</strong> Seal windows and doors. Use the air conditioner in recirculation mode.</li>
<li><strong>Air Purification:</strong> Run air purifiers at max speed in the room you occupy most.</li>
<li><strong>No Outdoor Exercise:</strong> Strictly avoid jogging or outdoor sports.</li>
<li><strong>Mask Up:</strong> If you must go out, wear an N95/N99 mask. Ensure a tight seal around the nose.</li>
<li><strong>Hydrate:</strong> Drink water to keep airways moist and help mucus clear particles.</li>
</ol>
</div>
<h3 class="section-header">Daily Safety Routine</h3>
<div class="neon-box">
<ul>
<li><strong>Monitor AQI:</strong> Check this app daily before leaving home.</li>
<li><strong>Ventilation Timing:</strong> Open windows only when AQI is lowest (usually mid-afternoon, depending on location).</li>
<li><strong>Clean Diet:</strong> Eat foods rich in Vitamin C, E, and Beta-carotene.</li>
<li><strong>Wash Up:</strong> Wash your face and rinse your eyes after coming from outside to remove settled particles.</li>
</ul>
</div>
<h3 class="section-header">Protective Gear Guide</h3>
<div class="neon-box">
<table class="glowing-table">
<tr>
<th style="color:#00f3ff">Mask Type</th>
<th style="color:#00f3ff">Protection Level</th>
<th style="color:#00f3ff">Usage</th>
</tr>
<tr>
<td>Cloth Mask</td>
<td>Low</td>
<td>Catches large dust only. Not effective for PM2.5.</td>
</tr>
<tr>
<td>Surgical Mask</td>
<td>Moderate</td>
<td>Fluid resistant, but loose fit allows leakage.</td>
</tr>
<tr>
<td>N95 / KN95</td>
<td>High (95%)</td>
<td>Filters 95% of airborne particles. Best for daily commute.</td>
</tr>
<tr>
<td>N99 / P100</td>
<td>Very High (99%+)</td>
<td>Near total filtration. Harder to breathe through for long periods.</td>
</tr>
</table>
</div>
<div class="neon-box">
<h4>When to seek Medical Help?</h4>
<p>Consult a doctor immediately if you experience:</p>
<ul>
<li>Persistent coughing or wheezing</li>
<li>Chest pain or tightness</li>
<li>Difficulty breathing even when resting</li>
<li>Severe eye irritation or vision changes</li>
</ul>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
