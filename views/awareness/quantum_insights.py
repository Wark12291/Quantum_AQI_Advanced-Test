import streamlit as st

def show_quantum_insights():
    st.markdown("<h1 class='neon-title'>⚛️ Quantum Computing in AQI</h1>", unsafe_allow_html=True)
    
    st.markdown("""
<div class="neon-box">
<h4>🤔 Why Quantum for Pollution?</h4>
<p>Classical computers struggle with complex chemical simulations. Quantum computers can simulate molecules exactly as they exist in nature.</p>
<ul>
<li><strong>Complex Interactions:</strong> Modeling how pollutants react with sunlight and other gases involves quantum mechanical processes that are hard to simulate classically.</li>
<li><strong>Optimization:</strong> Quantum algorithms can optimize logistics and traffic routes more efficiently to minimize emissions.</li>
</ul>
</div>
<h3 class="section-header">💻 The Simulation Workflow</h3>
<div class="neon-box">
<p>Our Quantum Module uses <strong>Qiskit</strong> to simulate noise and environmental effects.</p>
<ol>
<li><strong>Initialization:</strong> We prepare qubits in a superposition state using H-gates (Hadamard).</li>
<li><strong>Encoding:</strong> Environmental parameters (like temperature, humidity) are encoded into rotation angles.</li>
<li><strong>Noise Injection:</strong> We use depolarizing noise channels to simulate the chaotic nature of atmospheric data.</li>
<li><strong>Measurement:</strong> Collapsing the quantum state gives us probabilistic outcomes that can model uncertainty better than deterministc models.</li>
</ol>
</div>
<h3 class="section-header">🚪 Quantum Gates Used</h3>
<div class="neon-box">
<ul>
<li><strong>Hadamard (H):</strong> Creates superposition (0 and 1 at the same time), representing multiple atmospheric states simultaneously.</li>
<li><strong>RY Gate (Rotation Y):</strong> Rotates the qubit state to encode continuous variables like pollutant concentration.</li>
<li><strong>CNOT (CX):</strong> Entangles qubits to model correlations between different pollutants (e.g., how NO2 levels affect Ozone).</li>
</ul>
</div>
<div class="neon-box">
<h4>🚀 Future Applications</h4>
<p><strong>Catalyst Design:</strong> Quantum computers could help design new materials (catalysts) that can break down pollutants into harmless substances more efficiently than current technology.</p>
</div>
<a href="?nav=awareness_hub" target="_self">
<button class="awareness-back-btn">⬅ Back to Hub</button>
</a>
""", unsafe_allow_html=True)
