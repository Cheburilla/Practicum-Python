import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.write("# Информация о датасете")

st.sidebar.header("Информация о датасете")

df = pd.read_csv("data\\regression\\diamonds_prepared.csv")
df.drop(["Unnamed: 0"], axis=1, inplace=True)

col1, col2 = st.columns(2)

col1.dataframe(df)

col2.markdown(
    """
    Изначально этот классический набор данных содержит атрибуты почти 54 000 бриллиантов:
    * Цену в долларах (\$326 -- \$18,823) -- предсказываемый параметр

    * Количество карат (0.2--5.01)

    * Качество огранки (Fair, Good, Very Good, Premium, Ideal)

    * Цвет бриллианта

    * Чистота (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

    * Размеры по трём осям

    * Глубина = z / mean(x, y) = 2 * z / (x + y) (43--79)

    * Пропорция верхней части к самой широкой (43--95)
    """
)

st.markdown(
    """
    В процессе предобработки пришлось закодировать категориальные признаки (цвет, качество и чистоту) с помощью one-hot кодирования, поэтому признаковое пространство расширилось до 27 столбцов. Дубликатов, к счастью, оказалось меньше 100 штук на 54000 объектов.
    """
)
