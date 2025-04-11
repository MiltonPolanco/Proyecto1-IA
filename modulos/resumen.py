# modulos/resumen.py

import openai

def generar_resumen(texto: str, api_key: str) -> str:
    if not texto.strip():
        return "No hay suficiente contenido para generar un resumen."
        
    openai.api_key = api_key
    
    # Intenta usar el nuevo cliente si está disponible
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Resume el siguiente texto de manera concisa y clara."},
                {"role": "user", "content": texto}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    # Si falla, usa el método antiguo
    except (AttributeError, ImportError):
        try:
            response = openai.Completion.create(
                model="gpt-4o-mini",  # Modelo actualizado
                prompt=f"Resume el siguiente texto:\n\n{texto}",
                max_tokens=150,
                temperature=0.5
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error al generar resumen: {str(e)}")
            return f"Error al generar resumen: {str(e)}"