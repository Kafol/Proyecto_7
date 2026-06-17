# Importa la biblioteca Streamlit para crear aplicaciones web interactivas
import streamlit as st
import pandas as pd  # Importa la biblioteca Pandas para manipulación de datos
# Importa la biblioteca Plotly Graph Objects para crear gráficos personalizados
import plotly.graph_objects as go

# lee el archivo CSV con los datos de vehículos
car_data = pd.read_csv("vehicles_us.csv")
st.title("Análisis de Datos de Vehículos")  # Título de la aplicación Streamlit

# Crear un boton en Streamlit para mostrar el gráfico
his_button = st.button("Construir Histograma")

# Logica de ejecución del botón
if his_button:
    # Muestra un mensaje mientras se construye el histograma
    st.write("Construyendo el histograma...")
    # crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Construyendo el gráfico de dispersión...")
    # Crear un scatter plot utilizando plotly.graph_objects
    fig = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))
    # 'mode=markers' indica que queremos un gráfico de dispersión con puntos

    # Añade un título al gráfico
    fig.update_layout(title_text='Relación entre odómetro y precio')
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
