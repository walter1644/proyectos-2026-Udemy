# ========================================
# MÓDULO 5: recetas.py
# ========================================
import os
from pathlib import Path


def mostrar_recetas(ruta):
    """Muestra las recetas de una categoría y retorna una lista"""
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    if not lista_recetas:
        print("No hay recetas en esta categoria")

    return lista_recetas


def elegir_receta(lista):
    """Permite al usuario elegir una receta de la lista"""
    if not lista:
        return None
    
    eleccion_receta = 'x'

    while eleccion_receta.lower() != 'v' and (not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1)):
        eleccion_receta = input("\nElije una receta (o 'V' para volver): ")#problema aqui
    
    if eleccion_receta.lower() == 'v':
        return None
    
    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    """Lee y muestra el contenido de una receta"""
    print(Path.read_text(receta))


def crear_receta(ruta):
    """Crea una nueva receta en la categoría especificada"""
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")


def eliminar_receta(receta):
    """Elimina una receta"""
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")
