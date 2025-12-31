
import streamlit as st

def run():

    st.markdown("<h1 class='neon-title'>🛡 Precautions & Preventive Measures</h1>", unsafe_allow_html=True)
    st.write("")

    st.markdown("""
    Air pollution can cause immediate and long-term health issues.  
    These precautions help reduce daily exposure and protect overall well‑being.
    """)

    st.markdown("<h3 class='section-header'>🛣 Outdoor Precautions</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Outdoor environments often contain high levels of PM2.5, dust, and smoke.  
        Recommended outdoor safety steps:
        <ul>
            <li>Avoid heavy outdoor exercise during high AQI</li>
            <li>Wear N95/KN95 masks when outside</li>
            <li>Avoid highways, construction zones, and burning sites</li>
            <li>Prefer early afternoon for outdoor activity during polluted days</li>
            <li>Use AQI apps to check real-time air quality</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🏠 Indoor Precautions</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Indoor air quality can degrade quickly due to poor ventilation.  
        Protective steps include:
        <ul>
            <li>Use HEPA-based air purifiers to filter PM2.5 particles</li>
            <li>Keep windows closed during high pollution hours</li>
            <li>Avoid smoking, incense sticks, and chemical sprays indoors</li>
            <li>Clean fans, curtains, and vents regularly</li>
            <li>Ventilate your home only when AQI improves</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🚗 Travel & Commuting Precautions</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        When traveling, especially in polluted regions:
        <ul>
            <li>Use air-conditioned vehicles with air-recirculation mode</li>
            <li>Avoid two-wheelers during peak pollution hours</li>
            <li>Plan travel routes using AQI maps and forecasts</li>
            <li>Carry inhalers or medication if sensitive to pollution</li>
            <li>Avoid walking near traffic-heavy roads</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🩺 Medical & Health Precautions</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        People with existing health issues must take extra care:
        <ul>
            <li>Use doctor-prescribed inhalers and medications regularly</li>
            <li>Monitor oxygen levels during high AQI days</li>
            <li>Stay hydrated to help the body expel toxins</li>
            <li>Limit outdoor exposure as much as possible</li>
            <li>Consult a doctor if symptoms worsen</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🍵 Natural Remedies & Supportive Measures</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Natural remedies can help soothe the respiratory system:
        <ul>
            <li>Steam inhalation to clear nasal passages</li>
            <li>Warm water mixed with ginger and honey</li>
            <li>Turmeric milk for anti-inflammatory benefits</li>
            <li>Herbal teas (tulsi, mint, lemon, cinnamon)</li>
            <li>Eating antioxidant-rich foods (fruits, nuts, green vegetables)</li>
        </ul>
        These remedies support the body but do not replace medical treatment.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>📌 Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='neon-box'>
        Precautions play a vital role in reducing health risks associated with air pollution.  
        By taking small steps every day—like using masks, monitoring AQI, managing indoor air, and 
        avoiding exposure—you can significantly protect your health and well-being.
    </div>
    """, unsafe_allow_html=True)
