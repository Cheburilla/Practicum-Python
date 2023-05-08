import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(layout="wide")

st.write("# Визуализации")

st.sidebar.header("Визуализации")

df = pd.read_csv("data\\regression\\diamonds.csv")
dfp = pd.read_csv("data\\regression\\diamonds_prepared.csv")
df.drop(["Unnamed: 0"], axis=1, inplace=True)

plt.style.use('seaborn-v0_8-deep')
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
fig.set_facecolor('paleturquoise')
labels, counts = np.unique(df['cut'], return_counts=True)
axes[0][0].set_title('Круговая диаграмма качества огранки')
axes[0][0].pie(counts, labels=labels)
axes[1][0].set_title('Корреляция признаков', fontsize=14)
axes[0][1].set_title('Распределение цен бриллиантов')
sns.histplot(ax=axes[0][1], data=df['price'])
corr = dfp.corr()
sns.heatmap(corr, ax=axes[1][0], xticklabels=corr.columns, yticklabels=corr.columns, annot_kws={"size":10}) # type: ignore
axes[1][1].boxplot(x=df['depth'])
axes[1][0].set_title('Корреляция признаков', fontsize=14)
axes[1][1].set_title('Аномалии в глубине')
st.pyplot(fig)
