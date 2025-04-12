# 🧠 Asistente de Investigación Digital

Este proyecto es una aplicación web interactiva que actúa como un asistente de investigación digital. Permite a los usuarios ingresar un tema de interés y obtener información actualizada desde la web, procesarla mediante modelos de lenguaje, generar un resumen y visualizar una nube de palabras con los términos más relevantes.

---

## 🎯 Objetivo

El presente proyecto tiene como objetivo el desarrollo de una aplicación web interactiva que funcione como un asistente de investigación digital. Esta herramienta será capaz de buscar información actualizada en la web, analizarla utilizando modelos de lenguaje y presentar un resumen junto con una visualización interactiva de las palabras más frecuentes.

---

## 🚀 Funcionalidades

- Permitir al usuario ingresar un tema de interés desde la interfaz de usuario.
- Utilizar un agente ReAct de LangChain para realizar la búsqueda mediante Tavily.
- Mostrar los resultados encontrados en formato amigable (título, contenido parcial, enlace).
- Generar un resumen automático del contenido usando OpenAI (4 mini).
- Generar una nube de palabras (WordCloud) basada en el contenido recopilado.
- Presentar todos los resultados a través de una interfaz desarrollada en Streamlit.
- Modularizar el código en archivos separados dentro de una carpeta `/modulos`.
- Usar un archivo `.env` para proteger claves de API (se debe cargar sin incluir las claves reales).
- Incluir este archivo `README.md` con instrucciones para ejecución, descripción de módulos y una reflexión crítica.

---

## 🛠️ Tecnologías y Librerías Utilizadas

El proyecto utiliza las siguientes librerías y herramientas:

- `streamlit`: para crear la interfaz web.
- `requests`: para manejar solicitudes HTTP.
- `openai`: para generar resúmenes utilizando modelos de lenguaje.
- `python-dotenv`: para manejar variables de entorno de forma segura.
- `langchain`: para crear un agente ReAct que interactúa con la API de Tavily.
- `matplotlib`: para graficar la nube de palabras.
- `wordcloud`: para generar visualizaciones de términos frecuentes.

---


## Instalación

git clone https://github.com/MiltonPolanco/Proyecto1-IA.git nombre-carpeta
cd nombre-carpeta

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

pip install -r requirements.txt

OPENAI_API_KEY=tu_clave_openai
TAVILY_API_KEY=tu_clave_tavily

streamlit run app.py
