# Inventario simple basado en la consigna

inventario = []

def es_nombre_valido(nombre_texto):
    """Verifica que `nombre_texto` sea un nombre válido, no puede estar vacío ni ser
    solo espacios, devuelve `True` si cumple los criterios y `False` en caso
    contrario."""

    nombre_texto = nombre_texto.strip()
    if not nombre_texto:
        return False
    for parte in nombre_texto.split():
        if not parte.isalpha():
            return False
    return True

while True:
    nombre = input("Ingrese el nombre de la prenda: ").strip()
    if es_nombre_valido(nombre):
        nombre = nombre.lower()
        break
    print("Nombre inválido. Use solo letras y espacios. Intente de nuevo.")

def es_categoria_valida(categoria_texto):
    """Verifica que `categoria_texto` pertenezca a las categorías permitidas.

    Ignora mayúsculas y espacios al inicio/final. Devuelve True si es válida, False en caso contrario.
    """
    categoria_texto = categoria_texto.strip().lower()
    categorias_validas = {'remeras', 'pantalones', 'medias', 'calzoncillos'}
    return categoria_texto in categorias_validas

while True:
    categoria = input("Ingrese la categoría (remeras/pantalones/medias/calzoncillos): ").strip().lower()
    if es_categoria_valida(categoria):
        break
    print("Categoría inválida. Opciones válidas: remeras, pantalones, medias, calzoncillos. Intente de nuevo.")

def es_precio_valido(texto_precio):
    """Verifica que `texto_precio` represente un número (entero o decimal) no negativo.
    Devuelve True si la conversión a float es posible y el valor es > 0.
    """
    try:
        precio_convertido = float(texto_precio)
    except ValueError:
        return False
    return precio_convertido > 0


def es_stock_valido(texto_stock):
    """Verifica que `texto_stock` represente un entero no negativo.

    Intenta convertir a `int` usando un bloque try/except (igual que `es_precio_valido`),
    y verifica que el valor convertido sea >= 0.
    """
    try:
        stock_convertido = int(texto_stock.strip())
    except ValueError:
        return False
    return stock_convertido >= 0

def es_codigo_valido(texto_codigo):
    """Verifica que `texto_codigo` tenga exactamente 3 letras seguidas de 3 números.
    Convierte el texto a mayúsculas y ignora espacios al inicio/final.
    """
    import re
    texto_codigo = texto_codigo.strip().upper()
    return bool(re.fullmatch(r'[A-Z]{3}\d{3}', texto_codigo))

while True:
    precio_texto = input("Ingrese el precio: ").strip()
    if es_precio_valido(precio_texto):
        precio = round(float(precio_texto), 2)
        break
    print("Precio inválido. Ingrese un número no negativo (ej: 12.50). Intente de nuevo.")

while True:
    stock_texto = input("Ingrese la cantidad en stock: ").strip()
    if es_stock_valido(stock_texto):
        stock = int(stock_texto)
        break
    print("Stock inválido. Ingrese un entero no negativo. Intente de nuevo.")

while True:
    codigo = input("Ingrese el código del producto (ej: ABC123): ").strip().upper()
    if es_codigo_valido(codigo):
        break
    print("Código inválido. Debe tener 3 letras seguidas de 3 números (ej: ABC123). Intente de nuevo.")

producto = {
    "nombre": nombre,
    "categoria": categoria,
    "precio": precio,
    "stock": stock,
    "codigo": codigo
}

inventario.append(producto)

# Mostrar lo agregado
print("\nProducto agregado:")
print(f"  Nombre: {producto['nombre'].title()}")
print(f"  Categoría: {producto['categoria'].capitalize()}")
print(f"  Precio: ${producto['precio']:.2f}")
print(f"  Stock: {producto['stock']}")
print(f"  Código: {producto['codigo']}")
