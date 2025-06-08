# modulos/config.py

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Validar que las claves existen y tienen el formato correcto
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no encontrada en variables de entorno")
elif not OPENAI_API_KEY.startswith("sk-"):
    raise ValueError("OPENAI_API_KEY tiene formato inválido. Debe comenzar con 'sk-'")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY no encontrada en variables de entorno")

print(f"OpenAI API Key cargada: {OPENAI_API_KEY[:10]}...")  # Solo mostrar primeros 10 caracteres