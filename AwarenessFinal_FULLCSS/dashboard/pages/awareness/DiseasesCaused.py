
import streamlit as st

def run():

    st.markdown("<h1 class='neon-title'>🩺 Diseases Caused by Air Pollution</h1>", unsafe_allow_html=True)
    st.write("")

    st.markdown("""
    Air pollution is one of the leading environmental risk factors for disease worldwide.  
    Long-term exposure to polluted air significantly increases the risk of respiratory, cardiovascular, 
    neurological, and systemic health problems.  
    This page provides a detailed breakdown of diseases linked to high AQI levels.
    """)

    st.markdown("<h3 class='section-header'>🌬 Respiratory Diseases</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Air pollutants such as PM2.5, PM10, ozone, and nitrogen dioxide directly irritate the lungs, causing:
        <ul>
            <li><b>Asthma:</b> Increased frequency and severity of attacks</li>
            <li><b>Bronchitis:</b> Inflammation of airways leading to persistent cough</li>
            <li><b>Pneumonia:</b> Higher vulnerability to lung infections</li>
            <li><b>Reduced Lung Function:</b> Particularly dangerous for children</li>
            <li><b>Chronic Obstructive Pulmonary Disease (COPD)</b></li>
        </ul>
        High AQI days can immediately worsen breathing difficulty, especially among sensitive groups.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>❤️ Cardiovascular Diseases</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Pollutants such as PM2.5 and carbon monoxide enter the bloodstream and affect the heart:
        <ul>
            <li><b>Heart Attacks:</b> Higher risk due to reduced oxygen supply</li>
            <li><b>Hypertension:</b> Persistent exposure increases blood pressure</li>
            <li><b>Arrhythmias:</b> Irregular heartbeat due to toxic pollutants</li>
            <li><b>Stroke:</b> Blockage or bursting of blood vessels in the brain</li>
            <li><b>Worsening of Existing Heart Disease</b></li>
        </ul>
        Pollution is now considered a major risk factor for cardiovascular mortality.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🧠 Neurological Disorders</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Toxic particles can cross the blood–brain barrier, impacting mental and neurological health:
        <ul>
            <li><b>Headaches & Migraines</b></li>
            <li><b>Memory Loss:</b> Long-term exposure affects brain cells</li>
            <li><b>Reduced Concentration & Alertness</b></li>
            <li><b>Higher Risk of Alzheimer’s & Parkinson’s (emerging research)</b></li>
            <li><b>Delayed Brain Development in Children</b></li>
        </ul>
        Pollution affects both cognitive abilities and long-term neurological function.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🧬 Immune, Skin & Eye Diseases</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Air pollution weakens the immune system and damages exposed organs:
        <ul>
            <li><b>Allergic Reactions:</b> Increased sneezing, coughing, rashes</li>
            <li><b>Eye Irritation:</b> Redness, burning sensation, watery eyes</li>
            <li><b>Skin Aging:</b> Pollutants accelerate wrinkles and pigmentation</li>
            <li><b>Reduced Immunity:</b> Higher risk of viral and bacterial infections</li>
            <li><b>Chronic Fatigue:</b> Due to poor oxygen circulation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🧒 Sensitive Groups at Higher Risk</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Certain groups are significantly more vulnerable to pollution-related diseases:
        <ul>
            <li><b>Children:</b> Developing lungs and weaker immune systems</li>
            <li><b>Elderly:</b> Higher chance of chronic respiratory and heart issues</li>
            <li><b>Pregnant Women:</b> Risk of low birth weight & developmental issues</li>
            <li><b>People with Asthma or COPD</b></li>
            <li><b>Outdoor Workers:</b> Prolonged exposure to polluted air</li>
        </ul>
        These groups should take extra precautions on high AQI days.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>⚠ Long-Term Complications</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Prolonged exposure to polluted air can cause:
        <ul>
            <li><b>Permanent Lung Damage</b></li>
            <li><b>Chronic Heart Disease</b></li>
            <li><b>Neurological Degeneration</b></li>
            <li><b>Reduced Life Expectancy</b></li>
            <li><b>Increased Cancer Risk</b> (especially lung cancer)</li>
        </ul>
        Long-term exposure is the most dangerous form of pollution-related harm.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>📌 Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Air pollution affects almost every organ in the body, causing respiratory, cardiovascular, 
        neurological, and immune-related diseases. Understanding these risks helps individuals take 
        better preventive steps and protect long-term health.
    </div>
    """, unsafe_allow_html=True)
