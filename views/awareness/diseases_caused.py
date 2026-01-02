import streamlit as st

def show_diseases_caused():
    st.markdown("<h1 class='neon-title'>Diseases Linked to Pollution</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="alert-banner-red">
<h3>⚠️ Critical Health Warning</h3>
<p>“Air pollution doesn’t just harm nature — it causes global disease and medical crisis.”
</div>
<div class="neon-box">
<h4>Respiratory Diseases</h4>
<ul>
<li><strong>Asthma:</strong> Chronic inflammation of airways. Pollution triggers attacks and increases sensitivity to allergens.</li>
<li><strong>Chronic Bronchitis:</strong> Inflammation of the lining of bronchial tubes, causing daily cough and mucus production.</li>
<li><strong>Emphysema:</strong> Destruction of air sacs (alveoli) in lungs, causing shortness of breath.</li>
<li><strong>Lung Cancer:</strong> PM2.5 and certain toxic gases are classified as Group 1 carcinogens by IARC.</li>
</ul>
</div>
<h3 class="section-header">Cardiovascular Conditions</h3>
<div class="neon-box">
<ul>
<li><strong>Ischemic Heart Disease:</strong> Narrowed arteries reduce blood flow to the heart. Pollution accelerates plaque buildup.</li>
<li><strong>Stroke:</strong> Reduced blood flow to the brain due to clots or burst vessels.</li>
<li><strong>Heart Failure:</strong> The heart becomes too weak to pump blood effectively.</li>
</ul>
</div>
<h3 class="section-header">Child Health Issues</h3>
<div class="neon-box">
<ul>
<li><strong>Stunted Lung Growth:</strong> Children exposed to high pollution may never reach their full lung capacity potential.</li>
<li><strong>Pneumonia:</strong> Lower respiratory infections are a leading cause of death in children, exacerbated by dirty air.</li>
<li><strong>Cognitive Dvelopment:</strong> Emerging evidence suggests links to ADHD and lower IQ scores.</li>
</ul>
</div>
<div class="neon-box">
<h4>Other Complications</h4>
<p><strong>Diabetes:</strong> Air pollution is linked to increased risk of Type 2 diabetes due to inflammation and insulin resistance.</p>
<p><strong>Pregnancy Complications:</strong> Increased risk of miscarriage, stillbith, and low birth weight.</p>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
