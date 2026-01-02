import streamlit as st

def show_health_impact():
    st.markdown("<h1 class='neon-title'>❤️ Health Impact of Air Pollution</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>🫁 Respiratory System Effects</h4>
<p>Air pollution primarily attacks the respiratory system, causing both acute and chronic issues. Inhaling pollutants can irritate the airways, leading to coughing, wheezing, and shortness of breath.</p>
<ul>
<li><strong>Asthma Aggravation:</strong> Pollutants like ozone and PM2.5 can trigger asthma attacks and increase the frequency of symptoms.</li>
<li><strong>COPD (Chronic Obstructive Pulmonary Disease):</strong> Long-term exposure increases the risk of developing COPD and worsens the condition for those who already have it.</li>
<li><strong>Lung infections:</strong> Increased susceptibility to pneumonia and bronchitis.</li>
<li><strong>Reduced Lung Function:</strong> Studies show permanent reduction in lung capacity in children growing up in polluted areas.</li>
</ul>
</div>
<h3 class="section-header">💓 Cardiovascular Impact</h3>
<div class="neon-box">
<p>Fine particulate matter (PM2.5) can enter the bloodstream, traveling to the heart and causing systemic inflammation.</p>
<ul>
<li><strong>Heart Attacks:</strong> Short-term spikes in pollution are linked to an increased risk of myocardial infarction (heart attack).</li>
<li><strong>Stroke:</strong> Air pollution contributes to the hardening of arteries (atherosclerosis), increasing stroke risk.</li>
<li><strong>Hypertension:</strong> Chronic exposure is associated with higher blood pressure.</li>
<li><strong>Arrhythmias:</strong> Irregular heartbeats can be triggered by pollutant exposure.</li>
</ul>
</div>
<h3 class="section-header">🧠 Neurological & Other Effects</h3>
<div class="neon-box">
<p>Recent research suggests air pollution affects more than just lungs and heart:</p>
<ul>
<li><strong>Cognitive Decline:</strong> Studies link high pollution levels to faster cognitive decline in the elderly and potential links to Alzheimer's and Parkinson's diseases.</li>
<li><strong>Developmental Issues:</strong> Exposure during pregnancy can lead to low birth weight and preterm birth. It may also affect brain development in children.</li>
<li><strong>Eye Irritation:</strong> Symptoms like dryness, itching, and redness are common reactions to smog and high particulate levels.</li>
<li><strong>Skin Aging:</strong> Pollutants can accelerate skin aging, causing wrinkles and pigment spots.</li>
</ul>
</div>
<div class="neon-box">
<h4>🛡️ Who is Most at Risk?</h4>
<ul>
<li><strong>Children:</strong> Their lungs are still developing, and they breathe more air per pound of body weight.</li>
<li><strong>The Elderly:</strong> Often have weaker immune systems and pre-existing conditions.</li>
<li><strong>People with lung/heart disease:</strong> Their conditions make them more vulnerable to additional stress from pollution.</li>
<li><strong>Outdoor Workers:</strong> Have higher total exposure due to time spent outside.</li>
</ul>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
