import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---- Quantum Imports ----
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    QISKIT_AVAILABLE = True
except:
    QISKIT_AVAILABLE = False

def show_quantum():
    # Back to Home Navigation
    st.markdown("""
    <a href="?nav=home" target="_self">
        <button style="
            background: linear-gradient(45deg, #00f3ff, #bd00ff);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(189, 0, 255, 0.5);
        ">⬅ Back to Home</button>
    </a>
    <br><br>
    """, unsafe_allow_html=True)

    st.markdown("<h2 class='title-glow'>Quantum Pollution Simulation</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Quantum-inspired uncertainty modeling using AER Simulator</p>",
                unsafe_allow_html=True)

    if not QISKIT_AVAILABLE:
        st.error("❌ Qiskit is not installed. Add 'qiskit' to requirements.txt")
        return

    st.markdown("---")

    st.markdown("""
        <div style='display: flex; align-items: center; justify-content: space-between; width: 100%;'>
            <h3 style='margin: 0;'>⚙️ Quantum Circuit – Atmospheric Noise Simulation</h3>
            <div class='tooltip'>
                <span class='info-icon'>i</span>
                <span class='tooltiptext'>
                    <strong>Quantum Simulation Insight</strong><br>
                    This engine models atmospheric randomness by preparing a quantum bit in a state of superposition. 
                    <br><br>
                    <strong>Impacts:</strong><br>
                    Higher fluctuation (θ) shifts the probability towards |1⟩, representing increased pollution risk and higher simulated AQI values.
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Environmental randomness (user-controlled)
    theta = st.slider("Environmental Fluctuation (θ)", 0.0, 3.14, 1.2, 0.01)

    # -------------------------------
    # Quantum Simulation
    # -------------------------------
    with st.spinner("Running Quantum Calculation..."):
        qc = QuantumCircuit(1, 1)
        qc.h(0)              # base uncertainty
        qc.rx(theta, 0)      # environmental rotation
        qc.measure(0, 0)

        sim = AerSimulator()
        result = sim.run(qc, shots=1000).result()
        counts = result.get_counts()

        # Compute probabilities
        high_prob = counts.get('1', 0) / 1000  # higher pollution
        low_prob = counts.get('0', 0) / 1000   # lower pollution

        # Convert probability → AQI
        quantum_aqi = round(50 + high_prob * 250, 2)  # scale: 50→300

        # Noise Level
        noise_level = round(abs(np.sin(theta)), 2)

    # -------------------------------
    # Display Neon Output Cards
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
        <div class='neon-card'>
            <h3>🔮 High Pollution Probability</h3>
            <h2 style='color:#00eaff; text-shadow: 0 0 10px #00eaff;'>{round(high_prob*100,2)}%</h2>
        </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
        <div class='neon-card'>
            <h3>🌫 Quantum Simulated AQI</h3>
            <h2 style='color:#00ff88; text-shadow: 0 0 10px #00ff88;'>{quantum_aqi}</h2>
        </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
        <div class='neon-card'>
            <h3>🔉 Environmental Noise Level</h3>
            <h2 style='color:#ff007f; text-shadow: 0 0 10px #ff007f;'>{noise_level}</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # -------------------------------
    # Probability Bar Chart & Table
    # -------------------------------
    st.markdown("""
        <div style='background: rgba(0, 243, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid rgba(0, 243, 255, 0.1);'>
    """, unsafe_allow_html=True)
    
    c_chart, c_table = st.columns([0.6, 0.4])

    with c_chart:
        st.markdown("<h3 style='color:#00f3ff; text-shadow: 0 0 10px #00f3ff;'>📊 Quantum State Probability</h3>", unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(2.8, 1.8))
        categories = ["Low (|0⟩)", "High (|1⟩)"]
        values = [low_prob, high_prob]
        colors = ['#00ff88', '#ff007f']
        bar_width = 0.2  # Razor-thin width for a sharper look
        
        # Solid bars
        bars = ax.bar(categories, values, color=colors, alpha=1.0, width=bar_width)
        
        # Add labels with adjusted font size for micro frame
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{height*100:.1f}%', ha='center', va='bottom', 
                    color='white', fontweight='bold', fontsize=7,
                    bbox=dict(facecolor='#0b0f19', alpha=0.5, edgecolor='none', pad=0.2))

        # Styling - ultra compact
        ax.set_ylabel("Probability", color="white", fontsize=7, labelpad=2)
        ax.set_ylim(0, 1.1)
        fig.patch.set_facecolor("#0b0f19")
        ax.set_facecolor("#0a0e17")
        ax.tick_params(colors="white", labelsize=6, pad=2)
        
        # Neon Border & Grid
        for spine in ax.spines.values():
            spine.set_edgecolor("#00f3ff")
            spine.set_linewidth(2)
            spine.set_alpha(0.6)
            
        ax.grid(axis='y', color='#00f3ff', linestyle='--', alpha=0.15)
        plt.tight_layout()

        st.pyplot(fig)

    with c_table:
        st.markdown("<h3 style='color:#00f3ff; text-shadow: 0 0 10px #00f3ff;'>🔍 State Breakdown</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='margin-top:20px;'>
            <table class='glowing-table'>
                <thead>
                    <tr style='color:#00b7eb; text-align:left;'>
                        <th style='padding:12px; border-bottom: 1px solid rgba(0, 243, 255, 0.2);'>Quantum State</th>
                        <th style='padding:12px; border-bottom: 1px solid rgba(0, 243, 255, 0.2);'>Probability</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class='glow-cyan' style='font-size:1rem;'>|0⟩ – Low Pollution</td>
                        <td class='glow-green' style='font-size:1.3rem; font-weight:bold;'>{round(low_prob*100,2)}%</td>
                    </tr>
                    <tr>
                        <td class='glow-cyan' style='font-size:1rem;'>|1⟩ – High Pollution</td>
                        <td class='glow-pink' style='font-size:1.3rem; font-weight:bold;'>{round(high_prob*100,2)}%</td>
                    </tr>
                </tbody>
            </table>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.info("""
    **Interpretation:**
    - Quantum circuits model atmospheric randomness.
    - |1⟩ is mapped to higher pollution probability.
    - Noise level influences AQI fluctuations.
    - This provides a quantum-inspired stochastic pollution estimate.
    """)
