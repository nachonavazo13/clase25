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
    st.header('DATAFRAME')
    st.dataframe(df)
    st.header('TABLA')
    st.table(df)
    



# Crear ejecutable
if __name__ == "__main__":
    main()


