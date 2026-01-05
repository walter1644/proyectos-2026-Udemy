while True:
    producto = str(input("Ingresar el nombre del producto: ")).strip()
    if not producto:
        print("Nombre inválido. No puede estar vacío. Intenta de nuevo.")
        continue
    if any(character.isdigit() for character in producto):
        print("Nombre inválido. No uses números en el nombre del producto. Intenta de nuevo.")
        continue
    break

while True:
    try:
        precio = float(input("Ingrese su precio de compra: "))
        break
    except ValueError:
        print("Precio inválido. Intenta de nuevo (ej. 1500.50)")

# porcentaje de ganancia (puedes cambiarlo)
porcentaje = 50

# cálculos
precio_venta = precio * (1 + porcentaje / 100)
ganancia = precio_venta - precio

# salida formateada
print(f"Producto: {producto}")
print("-" * 50)
print(f"Precio de compra: ${precio:.2f}")
print("-" * 50)
print(f"Porcentaje de ganancia: {porcentaje}%")
print("-" * 50)
print(f"Precio de venta: ${precio_venta:.2f}")
print("-" * 50)
print(f"Ganancia por unidad: ${ganancia:.2f}")
print("-" * 50)
print("Gracias por usar el calculador de precios de venta.")