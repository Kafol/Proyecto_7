# Importa la biblioteca Streamlit para crear aplicaciones web interactivas
import streamlit as st
import pandas as pd  # Importa la biblioteca Pandas para manipulación de datos
# Importa la biblioteca Plotly Graph Objects para crear gráficos personalizados
import plotly.graph_objects as go

# lee el archivo CSV con los datos de vehículos
car_data = pd.read_csv("vehicles_us.csv")

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
