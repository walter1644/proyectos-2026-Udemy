"""Módulo principal del sistema bancario y punto de entrada de la aplicación."""

from interfaz import mostrar_bienvenida, mostrar_despedida
from servicios import busqueda_cliente, procesar_operacion


def main():
    """Función principal que inicia el sistema bancario"""
    mostrar_bienvenida()
    
    # Intentar crear o cargar cliente
    mi_cliente = None
    while mi_cliente is None:
        mi_cliente = busqueda_cliente()
        if mi_cliente is None:
            print("\n🔄 Reiniciando proceso de acceso...\n")
    
    print(f"\n{mi_cliente}")

    continuar = True
    while continuar:
        continuar = procesar_operacion(mi_cliente)
        
        # Verificar si el cliente aún existe después de la operación
        if continuar:
            from persistencia import cliente_existe
            if not cliente_existe(mi_cliente.numero_cuenta):
                print("\n⚠️  Su cuenta ha sido eliminada del sistema.")
                mostrar_despedida()
                return  # Termina el programa
            print(f"\n{mi_cliente}")
    mostrar_despedida()


if __name__ == "__main__":
    main()