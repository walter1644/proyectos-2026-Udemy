from random import randint

# Lista de prendas disponibles
prendas = ["remera", "pantalon", "campera", "buzo", "short", "vestido", "pollera", "camisa"]

intentos = 0
estimado = ""
indice_secreto = randint(0, len(prendas) - 1)
prenda_secreta = prendas[indice_secreto]

# Pedir nombre validando solo letras y espacios
while True:
    nombre = input("Dime tu nombre: ").strip()
    if nombre.replace(' ', '').isalpha():
        nombre = nombre.title()
        break
    print("Nombre inválido. Introduce solo letras y espacios.")

print(f"Bueno {nombre}, he pensado en una prenda de la lista")
print(f"Prendas disponibles: {', '.join(prendas)}")
print(f"Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = input("¿Cuál es la prenda?: ").lower().strip()
    intentos += 1

    if estimado == prenda_secreta:
        print(f"¡Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

    if estimado not in prendas:
        print("Esa prenda no está en la lista")
    elif estimado < prenda_secreta:
        print("Mi prenda está más adelante en la lista alfabéticamente")
    else:
        print("Mi prenda está más atrás en la lista alfabéticamente")

    # Pista: mostrar letra inicial y longitud
    longitud = len(prenda_secreta)
    unidad = "letra" if longitud == 1 else "letras"
    print(f"Pista: Empieza con '{prenda_secreta[0]}' y tiene {longitud} {unidad}.")

if estimado != prenda_secreta:
    print(f"Lo siento, se han agotado los intentos. La prenda secreta era: {prenda_secreta}")