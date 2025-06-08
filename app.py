# app.py

import streamlit as st
from modulos.busqueda import buscar_tavily
from modulos.resumen import generar_resumen
from modulos.wordcloud_gen import generar_nube_de_palabras
from modulos.config import TAVILY_API_KEY, OPENAI_API_KEY

def main():
    st.title("Asistente Digital de Investigación")
    
    # Verificar configuración de API keys
    if not OPENAI_API_KEY or not OPENAI_API_KEY.startswith("sk-"):
        st.error("⚠️ API Key de OpenAI no configurada correctamente")
        st.info("Por favor, configura tu API key en el archivo .env")
        return
    
    # Usar un formulario para manejar tanto Enter como el botón
    with st.form(key='search_form'):
        tema = st.text_input("Ingresa un tema de interés:")
        buscar_clicked = st.form_submit_button("Buscar")
    
    # Ejecutar la búsqueda si se presiona Enter o se hace clic en el botón
    if buscar_clicked and tema:
        # Realizar la búsqueda a través de la API de Tavily
        resultados = buscar_tavily(tema, TAVILY_API_KEY)
        
        # Procesar los resultados dentro del mismo bloque condicional
        if resultados:
            st.header("Resultados de la Búsqueda")
            
            # La API está devolviendo los resultados en la clave "results"
            if "results" in resultados and resultados["results"]:
                for item in resultados["results"]:
                    st.subheader(item.get("title", "Sin título"))
                    st.write(item.get("content", "Sin contenido"))
                    st.markdown(f"[Ver más]({item.get('url', '#')})")
                
                # Concatenar el contenido para el resumen y la nube de palabras
                texto_completo = " ".join([item.get("content", "") for item in resultados["results"]])
                
                # Verificar si hay suficiente texto para generar resumen y nube
                if texto_completo.strip():
                    # Generar resumen con manejo de errores
                    try:
                        resumen = generar_resumen(texto_completo, OPENAI_API_KEY)
                        st.header("Resumen Generado")
                        st.write(resumen)
                    except Exception as e:
                        st.error(f"Error al generar resumen: {str(e)}")
                        st.info("Verifica que tu API key de OpenAI sea válida y tenga créditos disponibles.")
                    
                    # Generar nube de palabras
                    try:
                        st.header("Nube de Palabras")
                        plt = generar_nube_de_palabras(texto_completo)
                        st.pyplot(plt.gcf())
                    except Exception as e:
                        st.error(f"Error al generar nube de palabras: {str(e)}")
                else:
                    st.warning("No hay suficiente contenido para generar resumen y nube de palabras.")
            else:
                st.warning("No se encontraron resultados para tu búsqueda.")
        else:
            st.error("No se pudieron obtener resultados de la búsqueda.")
    elif buscar_clicked and not tema:
        st.warning("Por favor, ingresa un tema para buscar.")

if __name__ == "__main__":
    main()