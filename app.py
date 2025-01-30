# python -m venv ev_streamlit25 como crear un entorno virtual
#ev_streamlit25\Scripts\activate asi activo el entorno virtual
# streamlit run app.py    asi ejecuto streamlit
# Con Ctrl + C cortamos la ejecucion


# importar las librerias

import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_excel('data/EQUIPOS_LNBP_MEXICO.xlsx')

# configuracion de la app
def main():
    # Comandos de Texto basicos
    st.title('App con Streamlit 25')
    # st.header('Este es el Header')
    # st.subheader('Este es el Subheader')
    # st.sidebar.title('Menu')
    # st.text('este seria un texto para la tabla')
    # st.subheader('Esta app permite visualizar datos de la NBA')
    # nombre = 'Ignacio'
    # st.text(f'El jugador destacado es {nombre}')
    # st.markdown('# Bebo')
    # st.markdown('## Bebo')
    # st.markdown('### Bebo')
    # st.markdown('#### Bebo')
    # st.markdown('##### Bebo')
    # st.success('No les demos nada, y quitemosles todo')
    # st.info('Esto es una informacion')
    # st.warning('Esto es un aviso')
    # st.error('Esto es un error')
    # st.help('Esto es ayuda')
    # st.write('el texto que querramos')
    
    
    # st.header('DATAFRAME')
    # st.dataframe(df)
    # st.header('TABLA')
    # st.table(df)

    # Trabajando con component
    # st.sidebar.image('data/nba_logo.png', width=200)
    posicion =st.selectbox('Seleccione una posicion', 
                 ["Armadores", "Aleros", "Internos"])
    
    st.write(f'La posicion es {posicion}')

    opcion = st.multiselect('Seleccione una posicion', 
                 ["Armadores", "Aleros", "Internos"])
    
    st.write(f'Las posiciones seleccionadas son {opcion}')


    edad = st.slider('Seleccione su edad',
                     min_value=18,
                     max_value=100, 
                     value=25,
                     step=1)
    
    st.write(f'Su edad es {edad}')


    nivel = st.select_slider('Seleccione su nivel',
                             options=["Muy bajo","Basico", "Intermedio", "Avanzado", "Super Avanzado"],)
    
    st.write(f'Su nivel es {nivel}')


    op = st.radio('Seleccione una opcion',  
                 ["Armadores", "Aleros", "Internos"])
    st.write(f'La opcion selecionada es {op}')


    check = st.checkbox('Acepto las condiciones')
    
    if check:
        st.success('Aceptaste las condiciones')
    else:
        st.error('Debe aceptar las condiciones')

    rta = st.button('Hola Nacho')
    
    if rta:
        st.success('Que haces crack')
    else:
        st.error('No ha pulsado el boton')

    tab1, tab2, tab3 = st.tabs(['Leones', 'Capitanes', 'Cangrejos'])

    with tab1:
        st.header('Leones de Pnce')
        st.image('assets/LEONES.png', width= 200)
    
    with tab2:
        st.header('Capitanes')
        st.image('assets/CAPITANES.png', width= 200)

    with tab3:
        st.header('Cangrejos')
        st.image('assets/CANGREJOS.png', width= 200)



    st.sidebar.text('Este es el sidebar')
    st.sidebar.selectbox('Seleccione una opcion', ['Opcion 1', 'Opcion 2', 'Opcion 3'])
    st.sidebar.multiselect('Seleccione varias opciones', ['Opcion 1', 'Opcion 2', 'Opcion 3'])
    st.sidebar.radio('Seleccione una opcion', ['Opcion 1', 'Opcion 2', 'Opcion 3'])
    st.sidebar.checkbox('Seleccione esta opcion', True)
    st.sidebar.number_input('Introduzca un numero', value=10)
    st.sidebar.slider('Rango de valores', 0, 100, 50)
    



# Crear ejecutable
if __name__ == "__main__":
    main()


