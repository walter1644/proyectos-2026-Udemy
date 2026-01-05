# ==================== utilidades.py ====================
"""
Módulo de funciones utilitarias.
Contiene funciones auxiliares para validación y entrada de datos
"""


def obtener_monto(mensaje):
    """
    Solicita un monto al usuario,si no ingresa nada retorna 0.0
    """
    while True:
        try:
            entrada = input(mensaje)
            if entrada.strip() == "":
                return 0.0
            monto = float(entrada)
            return monto
        except ValueError:
            print("Error: Por favor ingrese un número válido")


def obtener_texto(mensaje):
    """Solicita texto al usuario y lo limpia de espacios en blanco"""
    return input(mensaje).strip()


def mostrar_separador(caracter="=", longitud=40):
    """Muestra una línea separadora"""
    print(caracter * longitud)


def mostrar_titulo(titulo, caracter="=", longitud=40):
    """Muestra un título con separadores"""
    mostrar_separador(caracter, longitud)
    print(titulo)
    mostrar_separador(caracter, longitud)
