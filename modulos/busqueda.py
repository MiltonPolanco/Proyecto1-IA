# modulos/busqueda.py

import requests
import json

def buscar_tavily(consulta: str, api_key: str) -> dict:
    if not api_key:
        print("Error: TAVILY_API_KEY no está configurada")
        return {}
        
    url = "https://api.tavily.com/search"  # URL correcta de la API
    payload = {
        "api_key": api_key,
        "query": consulta,
        "search_depth": "advanced"
    }
    
    try:
        print(f"Enviando consulta a Tavily: {consulta}")
        response = requests.post(url, json=payload)
        
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text[:200]}...")  # Primeros 200 caracteres
        
        if response.status_code == 200:
            data = response.json()
            # Para depuración: muestra la estructura de los datos
            print(f"Estructura de datos: {json.dumps(data, indent=2)[:500]}")
            return data
        else:
            print(f"Error completo: {response.text}")
            return {}
    except Exception as e:
        print(f"Error al conectar con Tavily: {str(e)}")
        return {}