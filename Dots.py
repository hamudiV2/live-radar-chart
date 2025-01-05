import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Live Radar Chart")

# Input fields for scores
chem = st.number_input("Chemistry (%)", min_value=0, max_value=100, value=0)
bio = st.number_input("Biology (%)", min_value=0, max_value=100, value=0)
phy = st.number_input("Physics (%)", min_value=0, max_value=100, value=0)
eng = st.number_input("English (%)", min_value=0, max_value=100, value=0)
math = st.number_input("Maths (%)", min_value=0, max_value=100, value=0)

if st.button("Update Chart"):
    scores = [chem, bio, phy, eng, math]
    categories = ['Chemistry', 'Biology', 'Physics', 'English', 'Maths']
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    scores += scores[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True), facecolor='#0E1117')
    ax.set_facecolor('#0E1117')
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, color='white', size=12)
    plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="white", size=10)
    plt.ylim(0, 100)
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color='#1F77B4', label='Scores')
    ax.fill(angles, scores, color='#1F77B4', alpha=0.25)

    st.pyplot(fig)
