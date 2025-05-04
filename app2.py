import streamlit as st
import google.generativeai as genai
import os

# Configuración de la página
st.set_page_config(page_title="Chatbot con Gemini AI 2.0", page_icon="🤖")

# Función para inicializar el estado de la sesión
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "model" not in st.session_state:
        st.session_state.model = "gemini-2.0-pro-exp"

# Función para configurar la API de Gemini
def configure_genai():
    if st.session_state.api_key:
        try:
            genai.configure(api_key=st.session_state.api_key)
            # Verificar que el modelo está disponible
            model = genai.GenerativeModel(st.session_state.model)
            model.generate_content('test')
            return True
        except Exception as e:
            # Mostrar los modelos disponibles en caso de error
            try:
                available_models = genai.list_models()
                model_names = [model.name for model in available_models]
                st.error(f"Error al configurar la API: {str(e)}\n\nModelos disponibles:\n{', '.join(model_names)}")
            except Exception as list_error:
                st.error(f"Error al configurar la API: {str(e)}\nNo se pudieron obtener los modelos disponibles: {str(list_error)}")
            return False
    return False

# Función para generar respuesta
def generate_response(prompt):
    try:
        model = genai.GenerativeModel(st.session_state.model)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"

# Inicializar el estado de la sesión
initialize_session_state()

# Sidebar para configuración
with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("API Key de Gemini", type="password", value=st.session_state.api_key)
    if api_key:
        st.session_state.api_key = api_key
    
    model_option = st.selectbox(
        "Modelo",
        ("gemini-2.0-pro-exp", "gemini-1.5-pro", "gemini-pro-vision"),
        index=0
    )
    st.session_state.model = model_option
    
    if st.button("Limpiar conversación"):
        st.session_state.messages = []
        st.experimental_rerun()

# Título principal
st.title("Chatbot con Gemini AI 2.0 🤖")

# Verificar si la API está configurada
if not configure_genai():
    st.warning("Por favor, ingresa tu API Key de Gemini en la barra lateral para comenzar.")
    st.stop()

# Mostrar mensajes del chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = generate_response(prompt)
            st.markdown(response)
    
    # Agregar respuesta al historial
    st.session_state.messages.append({"role": "assistant", "content": response})