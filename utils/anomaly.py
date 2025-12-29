import pandas as pd

def detect_anomalies(df, threshold=1.5):
    """
    Detect anomalies using Z-Score or simple Moving Average deviation.
    Current Logic: Moving Average Deviation.
    """
    df['rolling_mean'] = df['AQI'].rolling(window=7).mean()
    df['deviation'] = df['AQI'] - df['rolling_mean']
    std_dev = df['deviation'].std()
    
    anomalies = df[abs(df['deviation']) > threshold * std_dev]
    
    return anomalies
