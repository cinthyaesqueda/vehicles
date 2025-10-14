# app.py
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r'C:\Users\admin\vehicles\vehicles_us.csv')

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

