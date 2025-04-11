# modulos/wordcloud_gen.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

def generar_nube_de_palabras(texto: str):
    # Verificar si el texto está vacío
    if not texto or not texto.strip():
        # Crear una figura vacía con un mensaje
        plt.figure(figsize=(10, 5))
        plt.text(0.5, 0.5, "No hay suficientes palabras para generar una nube", 
                 horizontalalignment='center', verticalalignment='center',
                 fontsize=14, color='gray')
        plt.axis("off")
        return plt
    
    # Si hay texto, generar la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt