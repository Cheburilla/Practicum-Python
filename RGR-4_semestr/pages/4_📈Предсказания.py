import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

st.set_page_config(layout="wide")

st.write("# Предсказания")

st.sidebar.header("Предсказания")

st.info(
    """
    Заполните _все_ характеристики, чтобы предсказать цену бриллианта.
    """
)

cut = st.select_slider(
    "Выберите качество",
    ("Fair (худшее)", "Good", "Very Good", "Premium", "Ideal (лучшее)"),
    "Very Good",
)

carat = st.slider("Выберите размер в каратах", 0.2, 5.02, 0.5)

clarity = st.select_slider(
    "Выберите чистоту",
    ("I1 (худшее)", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF (лучшее)"),
    "VS2",
)

color = st.select_slider(
    "Выберите цвет", ("J (худшее)", "I", "H", "G", "F", "E", "D (лучшее)"), "G"
)

x = st.slider("Выберите размер по оси x", 0.0, 10.0, 4.5)

y = st.slider("Выберите размер по оси y", 0.0, 10.0, 4.5)

z = st.slider("Выберите размер по оси z", 0.0, 10.0, 4.5)

depth = st.slider("Выберите глубину бриллианта", 40, 80, 55)

table = st.slider("Выберите отношение высота/ширина", 40, 100, 65)

if st.button("Submit"):
    df = pd.read_csv("data\\regression\\diamonds_prepared.csv")
    prediction = random.random() * 100 + random.random() * 10 + random.random()
    st.markdown(
        f"##### Бриллиант качества {cut}, размера {carat} карат, цвета {color}, с чистотой {clarity}, с размерами {x, y, z}, глубиной {depth} и пропорцией {table} обойдется вам всего лишь в {np.around(prediction, 2)}\$"
    )
