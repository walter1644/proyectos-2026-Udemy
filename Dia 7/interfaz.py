# ==================== interfaz.py ====================
"""
Módulo de interfaz de usuario
Contiene funciones para mostrar menús y interactuar con el usuario
"""
from constantes import (
    OPCION_DEPOSITAR, OPCION_RETIRAR, 
    OPCION_HISTORIAL, OPCION_SALIR
)
from utilidades import mostrar_titulo


def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print()
    mostrar_titulo("MENÚ DE OPERACIONES")
    print(f"({OPCION_DEPOSITAR}) Depositar")
    print(f"({OPCION_RETIRAR}) Retirar")
    print(f"({OPCION_HISTORIAL}) Ver historial")
    print(f"({OPCION_SALIR}) Salir")
    mostrar_titulo("", "=", 40)


def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida"""
    from constantes import MENSAJE_BIENVENIDA
    mostrar_titulo(MENSAJE_BIENVENIDA)


def mostrar_despedida():
    """Muestra el mensaje de despedida"""
    from constantes import MENSAJE_DESPEDIDA, MENSAJE_HASTA_PRONTO
    print()
    mostrar_titulo(MENSAJE_DESPEDIDA)
    print(MENSAJE_HASTA_PRONTO)
    mostrar_titulo("", "=", 40)

