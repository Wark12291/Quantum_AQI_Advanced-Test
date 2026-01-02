import streamlit as st

def show_understanding_aqi():
    st.markdown("<h1 class='neon-title'>📊 Understanding AQI</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>🤔 What is Air Quality Index (AQI)?</h4>
<p>The Air Quality Index (AQI) is a standard metric used by government agencies to communicate to the public how polluted the air currently is or how polluted it is forecast to become. As the AQI increases, an increasingly large percentage of the population is likely to experience increasingly severe adverse health effects.</p>
<p>Think of the AQI as a yardstick that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 represents good air quality with little potential to affect public health, while an AQI value over 300 represents hazardous air quality.</p>
</div>
<h3 class="section-header">📉 AQI Categories & Health Implications</h3>
<div class="neon-box">
<table class="glowing-table" style="width:100%">
<tr>
<th style="text-align:left; color:#00f3ff;">AQI Range</th>
<th style="text-align:left; color:#00f3ff;">Category</th>
<th style="text-align:left; color:#00f3ff;">Health Message</th>
</tr>
<tr>
<td style="color:#00ff88">0 - 50</td>
<td style="color:#00ff88">Good</td>
<td>Air quality is considered satisfactory, and air pollution poses little or no risk.</td>
</tr>
<tr>
<td style="color:#ffff00">51 - 100</td>
<td style="color:#ffff00">Moderate</td>
<td>Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people.</td>
</tr>
<tr>
<td style="color:#ffae00">101 - 150</td>
<td style="color:#ffae00">Unhealthy for Sensitive Groups</td>
<td>Members of sensitive groups may experience health effects. The general public is not likely to be affected.</td>
</tr>
<tr>
<td style="color:#ff0000">151 - 200</td>
<td style="color:#ff0000">Unhealthy</td>
<td>Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.</td>
</tr>
<tr>
<td style="color:#99004c">201 - 300</td>
<td style="color:#99004c">Very Unhealthy</td>
<td>Health alert: everyone may experience more serious health effects.</td>
</tr>
<tr>
<td style="color:#7e0023">301+</td>
<td style="color:#7e0023">Hazardous</td>
<td>Health warnings of emergency conditions. The entire population is more likely to be affected.</td>
</tr>
</table>
</div>
<h3 class="section-header">🧪 Key Pollutants Measured</h3>
<div class="neon-box">
<ul>
<li><strong>PM2.5 (Particulate Matter < 2.5 microns):</strong> Fine particles that can penetrate deep into the lungs and enter the bloodstream. Sources: Vehicle exhaust, industrial emissions, wildfires.</li>
<li><strong>PM10 (Particulate Matter < 10 microns):</strong> Larger particles that irritate eyes, nose, and throat. Sources: Dust, pollen, mold.</li>
<li><strong>Ozone (O3):</strong> Ground-level ozone is created by chemical reactions between oxides of nitrogen (NOx) and volatile organic compounds (VOC) in the presence of sunlight.</li>
<li><strong>Nitrogen Dioxide (NO2):</strong> From burning fuel (cars, trucks, buses, power plants). Irritates airways and aggravates respiratory diseases.</li>
<li><strong>Sulfur Dioxide (SO2):</strong> From burning fossil fuels and industrial processes. Harmful to the respiratory system.</li>
<li><strong>Carbon Monoxide (CO):</strong> Colorless, odorless gas from combustion processes. Reduces oxygen delivery to the body's organs.</li>
</ul>
</div>
<div class="neon-box">
<h4>🧮 How is AQI Calculated?</h4>
<p>The AQI is calculated for each pollutant individually using a formula that converts the concentration of the pollutant into a number on the 0-500 scale. The highest of these individual AQI numbers becomes the overall AQI for that location on that day.</p>
<p>The calculation involves specific "breakpoints" for each pollutant, which are established based on epidemiological studies of the health effects associated with different concentration levels.</p>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
