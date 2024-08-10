import pandas as pd
import plotly.express as px
import streamlit as st
        
#Primer paso: Leer el archivo CSV que se va a trabajar para el DataFrame
car_data = pd.read_csv('vehicles_us.csv')

#Segundo paso: Creación de un encabezado para la aplicación 
st.header('Análisis de vehículos en USA')

#Tercer paso: Creación de casilla de verificación. 
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: #Si la casilla de verifaciación esá seleccionada 
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer') #creación de un histograma
    st.plotly_chart(fig, use_container_width=True) #el proposito de esta función es mostrar un gráfico Plotly interactivo 

#Cuarto paso: Creación de una casilla de verifiación para la construcción de un gráfico de dispersión
build_scatter= st.checkbox('Creación de un gráfico de dispersión')

if build_scatter: #Si la casilla de verificación es seleccionada. 
    st.write('Creación de un gráfico de dispersión: precio vd oómetro.')
    fig=px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig,use_container_width=True)#el proposito de esta función es mostrar un gráfico Plotly interactivo 

    