# ========================================
# MÓDULO 6: main.py (Programa Principal)
# ========================================
from pathlib import Path

# Importar desde los módulos
from configuracion import MI_RUTA
from utilidades import limpiar_pantalla, contar_recetas, volver_inicio
from menu import mostrar_menu_principal
from categorias import mostrar_categorias, elegir_categoria, crear_categoria, eliminar_categoria
from recetas import mostrar_recetas, elegir_receta, leer_receta, crear_receta, eliminar_receta


def main():
    """Función principal del programa"""
    finalizar_programa = False

    while not finalizar_programa:
        # Limpiar pantalla y mostrar menú
        limpiar_pantalla()
        total_recetas = contar_recetas(MI_RUTA)
        menu = mostrar_menu_principal(MI_RUTA, total_recetas)

        # Opción 1: Leer receta
        if menu == 1:
            mis_categorias = mostrar_categorias(MI_RUTA)
            mi_categoria = elegir_categoria(mis_categorias)
            
            if mi_categoria is not None:
                mis_recetas = mostrar_recetas(mi_categoria)
                mi_receta = elegir_receta(mis_recetas)
                
                if mi_receta is not None:
                    leer_receta(mi_receta)
                    volver_inicio()

        # Opción 2: Crear receta nueva
        elif menu == 2:
            mis_categorias = mostrar_categorias(MI_RUTA)
            mi_categoria = elegir_categoria(mis_categorias)
            
            if mi_categoria is not None:
                crear_receta(mi_categoria)
                volver_inicio()

        # Opción 3: Crear categoría nueva
        elif menu == 3:
            if crear_categoria(MI_RUTA):
                volver_inicio()

        # Opción 4: Eliminar receta
        elif menu == 4:
            mis_categorias = mostrar_categorias(MI_RUTA)
            mi_categoria = elegir_categoria(mis_categorias)
            
            if mi_categoria is not None:
                mis_recetas = mostrar_recetas(mi_categoria)
                mi_receta = elegir_receta(mis_recetas)
                
                if mi_receta is not None:
                    eliminar_receta(mi_receta)
                    volver_inicio()

        # Opción 5: Eliminar categoría
        elif menu == 5:
            mis_categorias = mostrar_categorias(MI_RUTA)
            mi_categoria = elegir_categoria(mis_categorias)
            
            if mi_categoria is not None:
                eliminar_categoria(mi_categoria)
                volver_inicio()

        # Opción 6: Salir
        elif menu == 6:
            finalizar_programa = True


if __name__ == "__main__":
    main()
