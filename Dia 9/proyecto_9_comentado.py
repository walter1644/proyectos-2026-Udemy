import re  # Importa el módulo de expresiones regulares para buscar patrones en texto
import os  # Importa el módulo para interactuar con el sistema operativo (recorrer directorios)
import time  # Importa el módulo para medir tiempos de ejecución
import datetime  # Importa el módulo para trabajar con fechas y horas
from pathlib import Path  # Importa Path para manejar rutas de archivos de forma más elegante
import math  # Importa el módulo matemático (se usa para redondear hacia arriba)

inicio = time.time()  # Guarda el tiempo de inicio de la ejecución del programa

#ruta = 'C:\\Users\\Usuario\\Desktop\\Mi_Gran_Directorio'  (mal implementada)

ruta = r'C:\Users\walte\OneDrive\Desktop\proyectos 2026\Dia 9\Mi_Gran_Directorio'
# Define la ruta del directorio raíz a buscar


mi_patron = r'N\D{3}-\d{5}'  # Define el patrón regex: N + 3 caracteres NO dígitos + guión + 5 dígitos

hoy = datetime.date.today()  # Obtiene la fecha actual
nros_encontrados = []  # Lista vacía para almacenar los números de serie encontrados

archivos_encontrados = []  # Lista vacía para almacenar los nombres de archivos donde se encontraron números

def buscar_numero(archivo, patron):  # Define función que busca un patrón en un archivo
    try:
        with open(archivo, 'r', encoding='utf-8', errors='ignore') as este_archivo:
            texto = este_archivo.read()
            return re.search(patron, texto) or '' 
    except Exception as e: 
        return '' # Si el archivo no se puede leer, lo ignoramos

def crear_listas():  # Define función que recorre directorios y crea las listas de resultados
    for archivo in Path(ruta).rglob('*'):  # Itera sobre cada archivo en la carpeta actual y sus subcarpetas
            resultado = buscar_numero(archivo, mi_patron)  # Busca el patrón en el archivo actual
            if resultado:  # Si se encontró un número de serie
                nros_encontrados.append((resultado.group()))  # Agrega el número encontrado a la lista
                archivos_encontrados.append(archivo.name.title())  # Agrega el nombre del archivo en formato Title a la lista

#carpeta guarda ruta y 'a' guarda el nombre del archivo, luego se crea un objeto Path con ambos para abrir el archivo y buscar el patrón



def mostrar_todo():  # Define función que muestra los resultados en formato de tabla
    indice = 0  # Inicializa contador para sincronizar las dos listas
    print('-' * 50)  # Imprime línea separadora de 50 guiones
    print(f'Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')  # Imprime la fecha actual en formato dd/mm/aaaa
    print('\n') # Imprime línea en blanco
    
    
    if not nros_encontrados: # ✅ Verificación aquí print("No se encontraron números de serie en el directorio.") else:
        print("No se encontraron números de serie en el directorio.")
    else:
        print('ARCHIVO\t\tNRO. SERIE')  # Imprime encabezado de la tabla
        print('-------\t\t----------')  # Imprime separador del encabezado
        for a in archivos_encontrados:  # Itera sobre cada archivo encontrado
            print(f'{a}\t{nros_encontrados[indice]}')  # Imprime el titulo del archivo y su número de serie
            indice += 1  # Incrementa el índice para acceder al siguiente número de serie
    
    
    print('\n')  # Imprime línea en blanco
    print(f'Números encotrados: {len(nros_encontrados)}')  # Imprime la cantidad total de números encontrados
    fin = time.time()  # Guarda el tiempo de finalización del programa
    duracion = fin - inicio  # Calcula la duración total restando tiempo inicial del final
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')  # Imprime la duración redondeada hacia arriba
    print('-' * 50)  # Imprime línea separadora de 50 guiones

crear_listas()  # Ejecuta la función que busca y crea las listas de resultados
mostrar_todo()  # Ejecuta la función que muestra los resultados en pantalla
