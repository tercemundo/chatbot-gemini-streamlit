@echo off

REM Crear entorno virtual
python -m venv venv

REM Activar entorno
call venv\Scripts\activate

REM Instalar dependencias
pip install -r requirements.txt

REM Ejecutar aplicación
streamlit run app.py