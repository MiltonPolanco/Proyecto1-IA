# modulos/config.py

from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener claves API de las variables de entorno
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Verificar si las claves están disponibles
if not TAVILY_API_KEY:
    print("Advertencia: TAVILY_API_KEY no está configurada en el archivo .env")
if not OPENAI_API_KEY:
    print("Advertencia: OPENAI_API_KEY no está configurada en el archivo .env")