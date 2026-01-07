"""Módulo de funciones utilitarias.
Contiene funciones auxiliares para validación y entrada de datos"""


def obtener_monto(mensaje):
    """Solicita un monto al usuario,si no ingresa nada retorna 0.0"""
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
    """Solicita texto al usuario, lo limpia y valida que solo tenga letras"""
    while True:
        texto = input(mensaje).strip()
        if texto.isalpha():  # Comprueba que sean solo letras
            return texto
        else:
            print("Entrada inválida. Solo se permiten letras.")



def obtener_numero(mensaje):
    """Solicita números al usuario, los limpia y valida que solo tenga dígitos 0-9"""
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit():  # Comprueba que sean solo dígitos 0-9
            return texto
        else:
            print("Entrada inválida. Solo se permiten números.")


def mostrar_separador(caracter="=", longitud=40):
    """Muestra una línea separadora"""
    print(caracter * longitud)


def mostrar_titulo(titulo, caracter="=", longitud=40):
    """Muestra un título con separadores"""
    mostrar_separador(caracter, longitud)
    print(titulo)
    mostrar_separador(caracter, longitud)
