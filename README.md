# 🌐 Quantum AQI Advanced

> **Advanced Air Quality Index Forecasting Platform with AI & Quantum Computing**

A cutting-edge, full-stack web application for real-time air quality monitoring, AI-powered forecasting, and quantum-inspired pollution simulation. Built with modern technologies and designed for production deployment.

---

## ✨ Key Features

### 📊 **Real-Time Monitoring**

- Live AQI data from 20+ major Indian cities via WAQI API
- Interactive city-wise comparison and analysis
- Professional PDF report generation

### 🤖 **AI-Powered Forecasting**

- Hybrid ARIMA + LSTM models for 7-day predictions
- Statistical analysis with model performance metrics
- Automated trend detection and visualization

### ⚛️ **Quantum Simulation**

- Qiskit-powered atmospheric noise modeling
- Quantum state probability analysis
- AER Simulator integration for uncertainty quantification

### 🚨 **Anomaly Detection**

- Statistical spike detection using Z-score analysis
- Real-time alerts for pollution anomalies
- Historical trend analysis with rolling averages

### 🗺️ **Geospatial Visualization**

- Interactive heatmap with Folium integration
- Dark-themed maps for premium aesthetics
- City-level pollution distribution

### 🎨 **Premium UI/UX**

- Neon Cyber theme with glassmorphism effects
- Responsive design with smooth animations
- Professional data visualization with Plotly

---

## 🛠️ Technology Stack

| Category              | Technologies                      |
| --------------------- | --------------------------------- |
| **Framework**         | Streamlit                         |
| **Data Processing**   | Pandas, NumPy                     |
| **Machine Learning**  | Statsmodels (ARIMA), Scikit-Learn |
| **Quantum Computing** | Qiskit, Qiskit Aer                |
| **Visualization**     | Plotly, Folium, Matplotlib        |
| **API Integration**   | WAQI (World Air Quality Index)    |
| **PDF Generation**    | ReportLab                         |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd Quantum_AQI_Advanced
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`

---

## 📂 Project Structure

```
Quantum_AQI_Advanced/
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration and API settings
├── requirements.txt          # Python dependencies
├── views/                    # UI page modules
│   ├── home.py              # Landing page
│   ├── realtime.py          # Real-time AQI monitor
│   ├── forecasting.py       # AI forecasting module
│   ├── india_aqi.py         # India dashboard
│   ├── quantum.py           # Quantum simulation
│   ├── anomaly.py           # Anomaly detection
│   └── heatmap.py           # Geospatial heatmap
├── utils/                    # Helper modules
│   ├── api.py               # API integration
│   ├── forecasting.py       # ML models
│   ├── quantum.py           # Quantum algorithms
│   ├── anomaly.py           # Anomaly detection logic
│   └── pdf_gen.py           # PDF report generation
└── assets/                   # Static files
    └── style.css            # Custom styling
```

---

## 🌟 Features in Detail

### Real-Time AQI Monitor

- Fetch live pollution data for any city
- Display key pollutants (PM2.5, PM10, NO2, O3, SO2, CO)
- Weather integration (temperature, humidity, wind speed)
- Professional PDF report download

### AI Forecasting Engine

- 7-day ahead predictions using hybrid models
- ARIMA for time-series analysis
- LSTM for deep learning patterns
- Model performance metrics (AIC, BIC, HQIC)

### Quantum Pollution Simulation

- Quantum circuit-based noise modeling
- Probability distribution analysis
- Superposition state visualization
- AER Simulator backend

### Anomaly Detection System

- Z-score based statistical analysis
- Rolling average computation
- Automatic spike detection
- Historical anomaly log with expandable view

---

## 🔧 Configuration

Edit `config.py` to customize:

- API token for WAQI
- City list for monitoring
- Color scheme and theme settings

---

## 📊 Data Sources

- **WAQI API**: Real-time air quality data from monitoring stations worldwide
- **Simulated Historical Data**: For demonstration purposes (free API has rate limits)

---

## 🚀 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set main file: `app.py`
5. Deploy

For detailed deployment instructions, see `DEPLOYMENT_GUIDE.md`

---

## 📝 License

This project is open-source and available for educational and commercial use.

---

## 👤 Contact

**Developer**: Shadow  
**Telegram**: [@Shadow_5611](https://t.me/Shadow_5611)

For questions, suggestions, or collaboration opportunities, feel free to reach out!

---

## 🙏 Acknowledgments

- WAQI for providing free air quality data API
- Qiskit team for quantum computing framework
- Streamlit for the amazing web framework

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**
