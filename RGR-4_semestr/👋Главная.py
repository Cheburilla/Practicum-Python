import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.write("# Расчетно-графическая работа Сафронова Александра")

st.sidebar.info("Выберите страницу")

st.markdown(
    """
    Это главная страница РГР по машинному обучению за 4 семестр. 
    В боковом меню вы можете перейти на три страницы: 
    * Информация о датасете
    * Визуализации
    * Модели и предсказания
    """
)
