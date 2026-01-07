import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import utils.api as api
import utils.forecasting as forecasting

def show_forecasting():
    st.markdown("## Future AQI Forecasting")  

    st.markdown("""
    <a href="?nav=home" target="_self">
        <button class="awareness-back-btn">⬅ Back to Home</button>
    </a>
    """, unsafe_allow_html=True)
        
    st.write("Using ARIMA & LSTM Hybrid Model (Simulated Data for Demo)")
    
    # Get Data
    hist_data = api.get_historical_data_simulated(days=90)
    
    # Train Models
    with st.spinner("Training Models..."):
        arima_pred, arima_summary = forecasting.train_arima_model(hist_data['AQI'])
        lstm_pred = forecasting.train_lstm_model(hist_data['AQI'])
        hybrid = forecasting.get_hybrid_forecast(arima_pred, lstm_pred)
        
    # ---------------- 7-Day Forecast ----------------
    st.markdown("### 7-Day Forecast")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hist_data.index,
        y=hist_data['AQI'],
        mode='lines',
        name='Historical',
        line=dict(color='#00f3ff')
    ))
    fig.add_trace(go.Scatter(
        x=hybrid.index,
        y=hybrid,
        mode='lines+markers',
        name='Hybrid Forecast',
        line=dict(color='#bd00ff', dash='dot')
    ))
    
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title="AQI Trend & Prediction",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True)
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # ---------------- NEW: Past 30 Days Detailed Graph ----------------
    st.markdown("### Past 30 Days AQI Trend")

    past_30 = hist_data.tail(30)

    fig_past = go.Figure()
    fig_past.add_trace(go.Scatter(
        x=past_30.index,
        y=past_30['AQI'],
        mode='lines+markers',
        name='Daily AQI',
        line=dict(color='#00f3ff', width=2),
        marker=dict(size=6)
    ))

    fig_past.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=260,                     # Compact height
        title="Past 30 Days AQI Trend",
        xaxis=dict(
            showgrid=False,
            title=None,                 # ❌ Remove "Date" label
            tickformat="%b %d"
        ),
        yaxis=dict(
            showgrid=True,
            title="AQI"
        ),
        margin=dict(l=40, r=20, t=50, b=40)
    )

    st.plotly_chart(fig_past, use_container_width=True)

    # ---------------- ARIMA Summary ----------------
    with st.expander("View ARIMA Model Summary"):
        table_html = '<table style="width:100%; border-collapse: collapse; color: #e0e0e0; font-family: \'Segoe UI\', sans-serif;">'
        table_html += '<thead><tr style="border-bottom: 2px solid #00f3ff;">'
        table_html += '<th style="padding: 10px; text-align: left; color: #00f3ff;">Metric</th>'
        table_html += '<th style="padding: 10px; text-align: left; color: #00f3ff;">Value</th>'
        table_html += '</tr></thead><tbody>'
        
        if isinstance(arima_summary, dict):
            for key, value in arima_summary.items():
                try:
                    val_str = f"{value:.4f}" if isinstance(value, (float, np.floating)) else str(value)
                except:
                    val_str = str(value)
                    
                table_html += f'<tr style="border-bottom: 1px solid rgba(0, 243, 255, 0.2);">'
                table_html += f'<td style="padding: 10px; color: #bd00ff; font-weight: bold;">{key}</td>'
                table_html += f'<td style="padding: 10px;">{val_str}</td>'
                table_html += '</tr>'
        else:
            table_html += f"<tr><td colspan='2'>{arima_summary}</td></tr>"
            
        table_html += "</tbody></table>"
        st.write(table_html, unsafe_allow_html=True)
        
    # ---------------- Summary Cards ----------------
    c1, c2 = st.columns(2)
    with c1:
        avg_aqi = hybrid.mean()
        if not np.isnan(avg_aqi):
            st.success(f"Predicted Avg AQI (Next 7 Days): {int(round(avg_aqi))}")
        else:
            st.warning("Predicted Avg AQI: Data Unavailable")
    with c2:
        st.info("Accuracy: High (Simulated)")
