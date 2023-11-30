import nltk
import re
import json
from collections import defaultdict

# Descargar el recurso necesario para nltk si aún no lo tienes
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# Inicializar el lematizador de palabras
lemmatizer = WordNetLemmatizer()

# Función para obtener la raíz de una palabra usando lematización
def obtener_raiz(palabra):
    return lemmatizer.lemmatize(palabra)

# Función para procesar el archivo de URLs y generar el índice invertido de raíces de palabras
def crear_indice_invertido(urls_file):
    indice_invertido = defaultdict(lambda: defaultdict(int))

    with open(urls_file, 'r') as file:
        urls = file.readlines()

        for url in urls:
            # Realizar cualquier limpieza necesaria en la URL (eliminación de caracteres especiales, etc.)
            url = url.strip()

            # Aquí puedes agregar tu lógica para extraer las palabras de la URL
            # Utiliza expresiones regulares o cualquier otro método según la estructura de tus URLs
            words = re.findall(r'\w+', url)

            # Obtener la raíz de cada palabra y actualizar el índice invertido
            for word in words:
                root = obtener_raiz(word.lower())
                indice_invertido[root][url] += 1

    return indice_invertido

# Función para guardar el índice invertido en un archivo JSON
def guardar_indice_invertido(indice_invertido, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(indice_invertido, outfile, indent=2)

# Archivo de entrada y salida
input_file = 'urlsx.txt'
output_file = 'raiz_ind_inv.txt'

# Crear el índice invertido
indice_invertido = crear_indice_invertido(input_file)

# Transformar el índice invertido al formato deseado
output_format = []
for root, urls in indice_invertido.items():
    word_entry = {
        'palabra': root,
        'frecuencia_url': urls
    }
    output_format.append(word_entry)

# Guardar el índice invertido en el archivo de salida
guardar_indice_invertido(output_format, output_file)
