import streamlit as st
import utils.api as api
import utils.anomaly as anomaly
import plotly.express as px

def show_anomaly():
    st.markdown("## Anomaly Detection")
    
    st.markdown("""
    <a href="?nav=home" target="_self">
        <button class="awareness-back-btn">⬅ Back to Home</button>
    </a>
    """, unsafe_allow_html=True)
        
    st.write("Detecting sudden spikes in AQI levels using statistical analysis (Z-Score/Moving Average).")
    
    hist_data = api.get_historical_data_simulated(days=120) # 4 months
    
    anomalies = anomaly.detect_anomalies(hist_data)
    
    st.markdown(f"### Detected {len(anomalies)} Anomalies")
    
    fig = px.line(hist_data, x=hist_data.index, y='AQI', title="AQI History with Anomalies")
    fig.add_scatter(x=anomalies.index, y=anomalies['AQI'], mode='markers', name='Anomaly', marker=dict(color='red', size=10))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    if not anomalies.empty:
        # Sort latest to oldest
        anomalies_sorted = anomalies.sort_index(ascending=False)
        
        # Session state for expansion
        if 'show_all_anomalies' not in st.session_state:
            st.session_state.show_all_anomalies = False
            
        # Determine display data
        display_data = anomalies_sorted if st.session_state.show_all_anomalies else anomalies_sorted.head(5)
        
        # Polished, Diminished Table Representation
        table_html = f"""<div style='margin-top:20px;'>
<table style='width: 100%; border-collapse: collapse; border: 1px solid rgba(0, 243, 255, 0.1); color: #a0a0a0;'>
<thead>
<tr style='background: rgba(0, 243, 255, 0.05); color: #00f3ff; text-shadow: 0 0 5px rgba(0, 243, 255, 0.5);'>
<th colspan='4' style='padding: 12px; border-bottom: 2px solid rgba(0, 243, 255, 0.2); text-align: left; font-size: 0.95rem;'>
RECENT HIGH SEVERITY ANOMALIES LOG
</th>
</tr>
<tr style='text-align:left; font-size: 0.8rem; color: #808080; background: rgba(255, 255, 255, 0.02);'>
<th style='padding:10px; border-bottom: 1px solid rgba(255,255,255,0.1);'>DATE_LOG</th>
<th style='padding:10px; border-bottom: 1px solid rgba(255,255,255,0.1);'>VAL_AQI</th>
<th style='padding:10px; border-bottom: 1px solid rgba(255,255,255,0.1);'>R_MEAN</th>
<th style='padding:10px; border-bottom: 1px solid rgba(255,255,255,0.1);'>DEV_STAT</th>
</tr>
</thead>
<tbody>"""
        
        for idx, row in display_data.iterrows():
            date_str = idx.strftime('%d-%m-%Y %H:%M:%S')
            table_html += f"""<tr style='border-bottom: 1px solid rgba(255,255,255,0.05); font-family: "Courier New", monospace; font-size: 0.85rem;'>
<td style='padding:10px;'>{date_str}</td>
<td style='padding:10px; color: #00f3ff;'>{row['AQI']}</td>
<td style='padding:10px;'>{round(row['rolling_mean'], 2)}</td>
<td style='padding:10px; color: #ff004f; font-weight: bold;'>{round(row['deviation'], 2)}</td>
</tr>"""
            
        table_html += "</tbody></table></div>"
        
        st.markdown(table_html, unsafe_allow_html=True)
        
        # Toggle Button with Glassmorphism
        if len(anomalies_sorted) > 5:
            st.markdown("<div class='glass-button-container'>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([2, 1, 2])
            with col2:
                btn_label = "🔼 Show Less" if st.session_state.show_all_anomalies else "🔽 Show More"
                if st.button(btn_label, use_container_width=True):
                    st.session_state.show_all_anomalies = not st.session_state.show_all_anomalies
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success("No significant anomalies detected recently.")
