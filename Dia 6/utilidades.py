# ========================================
# MÓDULO 2: utilidades.py
# ========================================
from pathlib import Path
from os import system


def limpiar_pantalla():
    """Limpia la consola"""
    system('cls')


def contar_recetas(ruta):
    """Cuenta el total de archivos .txt en todas las subcarpetas"""
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def volver_inicio():
    """Pausa el programa hasta que el usuario presione 'V'"""
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ") #problema aqui