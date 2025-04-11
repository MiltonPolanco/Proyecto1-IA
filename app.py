# app.py

import streamlit as st
from modulos.busqueda import buscar_tavily
from modulos.resumen import generar_resumen
from modulos.wordcloud_gen import generar_nube_de_palabras
from modulos.config import TAVILY_API_KEY, OPENAI_API_KEY

def main():
    st.title("Asistente Digital de Investigación")
    
    # Entrada del usuario
    tema = st.text_input("Ingresa un tema de interés:")
    
    if st.button("Buscar"):
        if tema:
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
                        # Generar resumen
                        resumen = generar_resumen(texto_completo, OPENAI_API_KEY)
                        st.header("Resumen Generado")
                        st.write(resumen)
                        
                        # Generar nube de palabras
                        st.header("Nube de Palabras")
                        plt = generar_nube_de_palabras(texto_completo)
                        st.pyplot(plt.gcf())
                    else:
                        st.warning("No hay suficiente contenido para generar resumen y nube de palabras.")
                else:
                    st.warning("No se encontraron resultados para tu búsqueda.")
            else:
                st.error("No se pudieron obtener resultados de la búsqueda.")
        else:
            st.warning("Por favor, ingresa un tema para buscar.")

if __name__ == "__main__":
    main()