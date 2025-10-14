# app.py
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

DATA_PATH = Path(__file__).parent / "vehicles_us.csv"   # si el CSV está junto a app.py
# Si lo pusiste en carpeta data/: Path(__file__).parent / "data" / "vehicles_us.csv"

if not DATA_PATH.exists():
    st.error(f"No encuentro el archivo: {DATA_PATH}")
    st.stop()

car_data = pd.read_csv(DATA_PATH)

# Mostrar las primeras filas para verificar columnas
st.write("Vista previa de los datos:")
st.dataframe(car_data.head())


# ---------- Encabezado ----------
st.header("🚗 Exploración del Dataset de Vehículos")


# ---------- Botón para histograma ----------
if st.button("Mostrar histograma"):
    st.write("✅ Histograma generado con éxito:")

    fig = px.histogram(
        car_data,
        x="odometer",  
        nbins=20,
        title="Distribución del Odómetro de los Vehículos",
        color_discrete_sequence=["#4C78A8"]
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------- Botón para gráfico de dispersión ----------
elif st.button("Mostrar gráfico de dispersión"):
    st.write("✅ Dispersión generada con éxito:")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre Odómetro y Precio",
        color_discrete_sequence=["#E45756"]
    )

