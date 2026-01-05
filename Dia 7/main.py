# ==================== main.py ====================
"""
Módulo principal del sistema bancario
Punto de entrada de la aplicación
"""
from interfaz import mostrar_bienvenida, mostrar_despedida
from servicios import crear_cliente, procesar_operacion


def main():
    """Función principal que inicia el sistema bancario"""
    mostrar_bienvenida()
    
    # Intentar crear o cargar cliente
    mi_cliente = None
    while mi_cliente is None:
        mi_cliente = crear_cliente()
        if mi_cliente is None:
            print("\n🔄 Reiniciando proceso de acceso...\n")
    
    print(f"\n{mi_cliente}")

    continuar = True
    while continuar:
        continuar = procesar_operacion(mi_cliente)
        if continuar:
            print(f"\n{mi_cliente}")

    mostrar_despedida()


if __name__ == "__main__":
    main()