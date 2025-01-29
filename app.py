# python -m venv ev_streamlit25 como crear un entorno virtual
#ev_streamlit25\Scripts\activate asi activo el entorno virtual
# streamlit run app.py    asi ejecuto streamlit
# Con Ctrl + C cortamos la ejecucion


# importar las librerias

import streamlit as st
import pandas as pd
from PIL import Image

# configuracion de la app
def main():
    st.title('App con Streamlit 25')
    st.subheader('Esta app permite visualizar datos de la NBA')


# Crear ejecutable
if __name__ == "__main__":
    main()


