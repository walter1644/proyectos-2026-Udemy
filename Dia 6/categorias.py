# ========================================
# MÓDULO 4: categorias.py
# ========================================
import os
from pathlib import Path


def mostrar_categorias(ruta):
    """Muestra las categorías disponibles y retorna una lista de rutas"""
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        if carpeta.is_dir():
            carpeta_str = str(carpeta.name)
            print(f"[{contador}] - {carpeta_str}")
            lista_categorias.append(carpeta)
            contador += 1

    return lista_categorias


def elegir_categoria(lista):
    """Permite al usuario elegir una categoría de la lista"""
    eleccion_correcta = 'x'
    
    while eleccion_correcta.lower() != 'v' and (not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1)):
        eleccion_correcta = input("\nElije una categoria (o 'V' para volver): ") #problema aqui
    
    if eleccion_correcta.lower() == 'v':
        return None

    return lista[int(eleccion_correcta) - 1]

def crear_categoria(ruta):
    """Crea una nueva categoría (carpeta)"""
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria (o 'V' para volver): ") #problema aqui
        nombre_categoria = input()
        
        if nombre_categoria.lower() == 'v':
            return False
        
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")
    
    return True


def eliminar_categoria(categoria):
    """Elimina una categoría vacía"""
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")
