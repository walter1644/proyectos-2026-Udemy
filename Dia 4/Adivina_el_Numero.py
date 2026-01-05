from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)

# Pedir nombre validando solo letras y espacios
while True:
    nombre = input("Dime tu nombre: ").strip()
    if nombre.replace(' ', '').isalpha():
        nombre = nombre.title()
        break
    print("Nombre inválido. Introduce solo letras y espacios.")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    # Pedir número validando entero entre 1 y 100 (entradas inválidas no descuentan intento)
    while True:
        entrada = input(f"Intento {intentos+1}/8 - ¿Cuál es el número?: ").strip()
        try:
            estimado = int(entrada)
        except ValueError:
            print("Entrada inválida. Introduce solo números enteros.")
            continue
        if 1 <= estimado <= 100:
            break
        print("Número fuera de rango. Introduce un número entre 1 y 100.")

    intentos += 1

    if estimado < numero_secreto:
        print("Mi número es más alto")
    elif estimado > numero_secreto:
        print("Mi número es más bajo")
    else:
        print(f"¡Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El número secreto era {numero_secreto}")