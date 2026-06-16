import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="HBSC Dashboard", layout="wide")

st.markdown("""
    <style>
    /* Темна позадина како професионален дашборд */
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }

    /* Стилизирање на картичките */
    .card { background-color: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); }

    /* Боја на наслови */
    h1, h2, h3 { color: #00d2ff !important; font-family: 'Arial'; }

    /* Тргнување на sidebar-от и стандардни елементи */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("HBSC | Анализа на млади 2026")
st.markdown("---")

np.random.seed(42)
data = pd.DataFrame({'Возраст': np.random.choice([11, 12, 13, 14, 15], 300),
                     'Пол': np.random.choice(['Машки', 'Женски'], 300),
                     'Ниво на стрес (1-10)': np.random.randint(1, 11, 300)})
data['Часови спиење'] = 10 - (data['Ниво на стрес (1-10)'] * 0.3)

c1, c2 = st.columns(2)
with c1:
    selected_age = st.multiselect("Возраст:", [11, 12, 13, 14, 15], default=[11, 12, 13, 14, 15])
with c2:
    selected_gender = st.multiselect("Пол:", ['Машки', 'Женски'], default=['Машки', 'Женски'])

filtered_data = data[(data['Возраст'].isin(selected_age)) & (data['Пол'].isin(selected_gender))]

st.markdown("<br>", unsafe_allow_html=True)
c3, c4 = st.columns(2)

with c3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Корелација")
    fig = px.scatter(filtered_data, x='Ниво на стрес (1-10)', y='Часови спиење', color='Пол', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Стрес дистрибуција")
    fig2 = px.box(filtered_data, x='Возраст', y='Ниво на стрес (1-10)', color='Пол', template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.success("Ова решение е дизајнирано со фокус на User Experience и податочна визуелизација.")