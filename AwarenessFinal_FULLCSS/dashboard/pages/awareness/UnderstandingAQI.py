
import streamlit as st

def run():

    st.markdown("<h1 class='neon-title'>🌫 Understanding AQI (Air Quality Index)</h1>", unsafe_allow_html=True)
    st.write("")

    st.markdown("""
    The Air Quality Index (AQI) is a standardized system used worldwide to communicate how polluted 
    the air currently is or how polluted it is expected to become. AQI converts complex air pollutant 
    measurements into a single simple value ranging from 0 to 500, helping the public easily understand 
    the level of health risk associated with the air they breathe.
    """)

    st.markdown("<h3 class='section-header'>📘 What is AQI?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        AQI represents the concentration levels of major pollutants and expresses them as a unified 
        health-based index. It helps people determine whether outdoor activities are safe and whether 
        protective measures are needed.
        <br><br>
        Governments, researchers, and environmental agencies use AQI to:
        <ul>
            <li>Monitor real-time pollution</li>
            <li>Assess health impact</li>
            <li>Improve environmental planning</li>
            <li>Take emergency pollution-control actions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🧪 Major Pollutants Included in AQI</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        AQI is calculated using the concentration levels of six major pollutants:
        <ul>
            <li><b>PM2.5</b> – Fine particulate matter</li>
            <li><b>PM10</b> – Coarse particulate matter</li>
            <li><b>O₃</b> – Ground-level ozone</li>
            <li><b>NO₂</b> – Nitrogen Dioxide</li>
            <li><b>SO₂</b> – Sulfur Dioxide</li>
            <li><b>CO</b> – Carbon Monoxide</li>
        </ul>
        These pollutants have the highest impact on respiratory and cardiovascular health.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>📊 AQI Ranges & Categories</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        AQI is divided into six color-coded categories:
        <ul>
            <li><b>0–50 (Good)</b> – Clean air, minimal risk</li>
            <li><b>51–100 (Satisfactory)</b> – Acceptable air quality</li>
            <li><b>101–200 (Moderate)</b> – Some discomfort for sensitive groups</li>
            <li><b>201–300 (Poor)</b> – Breathing irritation for most people</li>
            <li><b>301–400 (Very Poor)</b> – Serious respiratory concerns</li>
            <li><b>401–500 (Severe)</b> – Hazardous & emergency conditions</li>
        </ul>
        Higher AQI values represent higher pollution levels and increased health risks.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🧮 How is AQI Calculated?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        AQI is calculated using pollutant concentration values measured by monitoring stations.  
        Each pollutant is converted into an individual sub-index using standard formulas, and the 
        highest sub-index becomes the overall AQI.
        <br><br>
        <b>Overall AQI = Max (Sub-index of PM2.5, PM10, O₃, NO₂, SO₂, CO)</b>
        <br><br>
        This ensures that the most harmful pollutant of the moment determines the AQI for public safety.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🎯 Why AQI Matters</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        AQI helps individuals:
        <ul>
            <li>Plan outdoor activities safely</li>
            <li>Protect children, elders, and asthma patients</li>
            <li>Avoid polluted areas during peak times</li>
            <li>Use masks and purifiers when needed</li>
            <li>Understand long-term environmental trends</li>
        </ul>
        AQI empowers the public with real-time environmental awareness.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>📌 Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        The Air Quality Index is a simple but powerful indicator of air pollution and health risk.  
        Understanding AQI helps people stay safe, make informed decisions, and contribute to a 
        cleaner environment.
    </div>
    """, unsafe_allow_html=True)
