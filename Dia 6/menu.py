# ========================================
# MÓDULO 3: menu.py
# ========================================
def mostrar_menu_principal(ruta, total_recetas):
    """Muestra el menú principal y retorna la opción elegida"""
    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en {ruta}")
    print(f"Total recetas: {total_recetas}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)
