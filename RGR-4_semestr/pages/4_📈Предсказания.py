import pickle
import random

import numpy as np
import pandas as pd
from sklearn import model_selection
import streamlit as st
import tensorflow as tf

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
    ("Fair", "Good", "Very Good", "Premium", "Ideal"),
    "Very Good",
)

carat = st.slider("Выберите размер в каратах", 0.2, 5.02, 0.5)

clarity = st.select_slider(
    "Выберите чистоту",
    ("I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"),
    "VS2",
)

color = st.select_slider("Выберите цвет", ("J", "I", "H", "G", "F", "E", "D"), "G")

x = st.slider("Выберите размер по оси x", 0.0, 10.0, 4.5)

y = st.slider("Выберите размер по оси y", 0.0, 10.0, 4.5)

z = st.slider("Выберите размер по оси z", 0.0, 10.0, 4.5)

depth = st.slider("Выберите глубину бриллианта", 40, 80, 55)

table = st.slider("Выберите отношение высота/ширина", 40, 100, 65)

regressor = st.selectbox(
    "Выберите регрессор", ("DecisionTree", "Bagging", "TensorFlow"), 0
)

if st.button("Предсказать!"):
    columns = [
        "carat",
        "depth",
        "table",
        "x",
        "y",
        "z",
        "ct_Fair",
        "ct_Good",
        "ct_Ideal",
        "ct_Premium",
        "ct_Very Good",
        "clr_D",
        "clr_E",
        "clr_F",
        "clr_G",
        "clr_H",
        "clr_I",
        "clr_J",
        "clrty_I1",
        "clrty_IF",
        "clrty_SI1",
        "clrty_SI2",
        "clrty_VS1",
        "clrty_VS2",
        "clrty_VVS1",
        "clrty_VVS2",
    ]
    df = pd.DataFrame(
        [[carat, depth, table, x, y, z, *[0 for i in range(20)]]], columns=columns
    )
    for a in df.columns[7:11]:
        if cut in a:
            df[a] = 1
    for a in df.columns[12:18]:
        if color in a:
            df[a] = 1
    for a in df.columns[19:26]:
        if clarity == a[6:]:
            df[a] = 1
    models = {
        "DecisionTree": "models/decisiontreeregressor.pickle",
        "Bagging": "models/baggingregressor.pickle",
        "TensorFlow": "models/tensorflowregressor.h5",
    }
    prediction = random.random() * 100 + random.random() * 10 + random.random()
    if regressor != "TensorFlow":
        with open(models.get(regressor), "rb") as f:  # type: ignore
            model = pickle.load(f)
            model_columns = model.feature_names_in_
            df.columns = model_columns
    else:
        model = tf.keras.models.load_model(models.get(regressor))
    prediction = float(model.predict(df))  # type: ignore

    st.markdown(
        f"##### Бриллиант качества {cut}, размера {carat} карат, цвета {color}, с чистотой {clarity}, с размерами {x, y, z}, глубиной {depth} и пропорцией {table} обойдется вам всего лишь в {np.around(prediction, 2)}\$"
    )
