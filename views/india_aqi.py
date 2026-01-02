import streamlit as st
import utils.api as api
import utils.pdf_gen as pdf_gen
import pandas as pd
import plotly.express as px
from datetime import datetime

def show_india_aqi():
    st.markdown("## India AQI Analysis")
    
    st.markdown("""
    <a href="?nav=home" target="_self">
        <button class="awareness-back-btn">⬅ Back to Home</button>
    </a>
    """, unsafe_allow_html=True)
        
    st.info("Fetching data for major Indian cities. Please wait...")
    
    df = api.fetch_all_cities_aqi()
    
    if not df.empty:
        # Sort by AQI ascending (lowest to highest) as requested for Detailed Data
        dfSorted = df.sort_values(by="AQI", ascending=True)
        
        # Add AQI Category for enhancement
        def get_category(aqi):
            if aqi <= 50: return "Good"
            if aqi <= 100: return "Moderate"
            if aqi <= 150: return "Unhealthy for Sensitive Groups"
            if aqi <= 200: return "Unhealthy"
            if aqi <= 300: return "Very Unhealthy"
            return "Hazardous"
        
        dfSorted['Category'] = dfSorted['AQI'].apply(get_category)
        
        st.markdown("### Top Polluted vs Cleanest")
        c1, c2 = st.columns(2)
        with c1:
            most_polluted = dfSorted.iloc[-1]
            st.error(f"Most Polluted: **{most_polluted['City']}** (AQI: {most_polluted['AQI']})")
        with c2:
            cleanest = dfSorted.iloc[0]
            st.success(f"Cleanest: **{cleanest['City']}** (AQI: {cleanest['AQI']})")
            
        st.markdown("### 📊 City AQI Comparison")
        fig = px.bar(
            dfSorted, x='City', y='AQI', 
            color='AQI', 
            color_continuous_scale=['green', 'yellow', 'orange', 'red', 'purple', 'maroon'],
            template="plotly_dark",
            title="AQI Levels Across Major Cities"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Custom Header for Detailed Data with PDF Icon
        st.markdown("<br>", unsafe_allow_html=True)
        col_title, col_download = st.columns([0.85, 0.15])
        
        with col_title:
            st.markdown("### 📋 Detailed Data")
        
        with col_download:
            # Generate the PDF buffer
            pdf_buffer = pdf_gen.generate_enhanced_pdf_report(
                title="India Air Quality Index (AQI) - Detailed Report",
                metadata=[
                    f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    "Source: WAQI Real-time Monitoring Network"
                ],
                summary_stats=[
                    f"Average India AQI: {int(dfSorted['AQI'].mean())}",
                    f"Most Polluted City: {most_polluted['City']} (AQI: {most_polluted['AQI']})",
                    f"Cleanest City: {cleanest['City']} (AQI: {cleanest['AQI']})"
                ],
                df=dfSorted
            )
            
            # CSS to make the button look more like a standalone icon/symbol in the top right
            st.markdown("""
                <style>
                    div[data-testid="stDownloadButton"] {
                        text-align: right;
                    }
                    div[data-testid="stDownloadButton"] button {
                        background: linear-gradient(45deg, #00f3ff, #00b7eb) !important;
                        color: white !important;
                        border: none !important;
                        padding: 8px 20px !important;
                        font-size: 14px !important;
                        font-weight: bold !important;
                        border-radius: 8px !important;
                        box-shadow: 0 0 10px rgba(0, 243, 255, 0.4) !important;
                        transition: all 0.3s ease !important;
                    }
                    div[data-testid="stDownloadButton"] button:hover {
                        box-shadow: 0 0 20px rgba(0, 243, 255, 0.7) !important;
                        transform: scale(1.05) !important;
                    }
                    /* Hide default dataframe toolbar to focus on our Professional PDF */
                    [data-testid="stElementToolbar"] {
                        display: none;
                    }
                </style>
            """, unsafe_allow_html=True)
            
            st.download_button(
                label="Download",
                data=pdf_buffer,
                file_name=f"India_AQI_Report_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime='application/pdf',
                key="header_pdf_download"
            )

        st.dataframe(dfSorted.drop(columns=['Category']), hide_index=True, use_container_width=True)
    else:
        st.warning("Could not fetch data.")
