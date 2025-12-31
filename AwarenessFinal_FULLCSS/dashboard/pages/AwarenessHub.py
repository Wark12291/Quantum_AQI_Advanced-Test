
import streamlit as st

def run():
    st.markdown("<h1 class='neon-title'>🧠 AQI Awareness & Safety Hub</h1>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""Explore essential air-quality awareness topics, safety measures,
    environmental strategies, and quantum insights — all organized into interactive neon cards.""")
    st.write("")

    # CSS for Cards
    st.markdown("""
    <style>
    .hub-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 25px;
        margin-top: 20px;
    }
    .hub-card {
        background: rgba(0, 20, 45, 0.60);
        border: 1px solid #00aaff;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        cursor: pointer;
        transition: 0.25s;
        box-shadow: 0 0 10px rgba(0, 170, 255, 0.4);
    }
    .hub-card:hover {
        transform: scale(1.04);
        box-shadow: 0 0 22px rgba(0, 200, 255, 0.85);
        border-color: #33ccff;
    }
    .hub-card h3 {
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin-top: 18px;
        margin-bottom: 8px;
        text-shadow: 0 0 6px #0099ff;
    }
    .hub-card p {
        color: #d0ecff;
        font-size: 15px;
        line-height: 1.4;
    }
    @media (max-width: 900px) {
        .hub-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 500px) {
        .hub-grid { grid-template-columns: repeat(1, 1fr); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='hub-grid'>", unsafe_allow_html=True)

    # ----- Card 1 -----
    if st.button("Understanding AQI", key="c1"):
        st.session_state["awareness_page"] = "UnderstandingAQI"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c1').click()">
            <h3>Understanding AQI</h3>
            <p>Learn how AQI works, pollutant categories, and meaning of AQI levels.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 2 -----
    if st.button("Health Impact", key="c2"):
        st.session_state["awareness_page"] = "HealthImpact"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c2').click()">
            <h3>Health Impact</h3>
            <p>Explore how air pollution affects lungs, heart, brain, and overall health.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 3 -----
    if st.button("Precautions", key="c3"):
        st.session_state["awareness_page"] = "Precautions"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c3').click()">
            <h3>Precautions</h3>
            <p>Daily safety measures to reduce exposure and stay protected.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 4 -----
    if st.button("Pollution Control", key="c4"):
        st.session_state["awareness_page"] = "PollutionControl"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c4').click()">
            <h3>Pollution Control</h3>
            <p>Solutions for individuals, communities, industries & governments.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 5 -----
    if st.button("AQI Devices", key="c5"):
        st.session_state["awareness_page"] = "AQIDevices"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c5').click()">
            <h3>AQI Devices</h3>
            <p>Explore advanced sensors and smart monitoring technologies.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 6 -----
    if st.button("Quantum Insights", key="c6"):
        st.session_state["awareness_page"] = "QuantumInsights"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c6').click()">
            <h3>Quantum Insights</h3>
            <p>Understand how quantum computing simulates pollution uncertainty.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 7 -----
    if st.button("Citizen Role", key="c7"):
        st.session_state["awareness_page"] = "CitizenRole"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c7').click()">
            <h3>Citizen Role</h3>
            <p>Discover how people can contribute to cleaner air.</p>
        </div>
    """, unsafe_allow_html=True)

    # ----- Card 8 -----
    if st.button("AQI Monitoring", key="c8"):
        st.session_state["awareness_page"] = "AQIMonitoring"
    st.markdown("""
        <div class='hub-card' onclick="document.getElementById('c8').click()">
            <h3>AQI Monitoring</h3>
            <p>Learn why daily and long-term AQI monitoring is important.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------- Routing Logic -------------
    if "awareness_page" in st.session_state:
        pg = st.session_state["awareness_page"]

        if pg == "UnderstandingAQI":
            from dashboard.pages.awareness.UnderstandingAQI import run as p
            p()

        elif pg == "HealthImpact":
            from dashboard.pages.awareness.HealthImpact import run as p
            p()

        elif pg == "Precautions":
            from dashboard.pages.awareness.Precautions import run as p
            p()

        elif pg == "PollutionControl":
            from dashboard.pages.awareness.PollutionControl import run as p
            p()

        elif pg == "AQIDevices":
            from dashboard.pages.awareness.AQIDevices import run as p
            p()

        elif pg == "QuantumInsights":
            from dashboard.pages.awareness.QuantumInsights import run as p
            p()

        elif pg == "CitizenRole":
            from dashboard.pages.awareness.CitizenRole import run as p
            p()

        elif pg == "AQIMonitoring":
            from dashboard.pages.awareness.AQIMonitoring import run as p
            p()
