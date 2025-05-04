# Chatbot con Gemini AI 2.5 🚀

Este es un chatbot interactivo construido con Streamlit y la API de Google Gemini AI. El chatbot permite mantener conversaciones utilizando diferentes modelos de Gemini, incluyendo la última versión 2.5.

## Requisitos Previos

- Python 3.7 o superior
- Cuenta de Google AI Studio con acceso a la API de Gemini
- API Key de Gemini

## Instalación

1. Clona o descarga este repositorio en tu máquina local

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. Instala las dependencias necesarias:
```bash
pip install streamlit google-generativeai
```

## Configuración de la API Key

1. Visita [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea o selecciona un proyecto
3. Genera una nueva API Key
4. Guarda la API Key de forma segura

## Ejecución del Chatbot

1. Asegúrate de que el entorno virtual está activado

2. Ejecuta la aplicación:
```bash
streamlit run app3.py
```

3. Se abrirá automáticamente una ventana del navegador con la interfaz del chatbot

4. En la barra lateral, ingresa tu API Key de Gemini

5. Selecciona el modelo que deseas utilizar:
   - gemini-2.5-pro-exp-03-25 (última versión)
   - gemini-2.0-pro-exp
   - gemini-1.5-pro
   - gemini-pro-vision

6. ¡Comienza a chatear!

## Características

- Interfaz de usuario intuitiva y amigable
- Soporte para múltiples modelos de Gemini
- Historial de conversación persistente
- Opción para limpiar el historial de chat
- Manejo de errores y visualización de modelos disponibles
- Diseño responsive

## Notas de Uso

- La API Key se almacena temporalmente en la sesión de Streamlit
- Puedes cambiar de modelo en cualquier momento durante la conversación
- El botón "Limpiar conversación" elimina todo el historial de chat
- Si ocurre algún error, el sistema mostrará los modelos disponibles

## Seguridad

- No compartas tu API Key
- La API Key se ingresa en un campo de tipo password para mayor seguridad
- No se almacena permanentemente ninguna información sensible

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor crea un issue en el repositorio.