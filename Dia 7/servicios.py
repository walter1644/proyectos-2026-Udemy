# ==================== servicios.py ====================
"""
Módulo de servicios bancarios
Contiene la lógica de negocio para operaciones bancarias
"""
from modelos import Cliente
from utilidades import obtener_monto, obtener_texto, mostrar_titulo
from constantes import (
    OPCION_DEPOSITAR, OPCION_RETIRAR,
    OPCION_HISTORIAL, OPCION_SALIR
)
from interfaz import mostrar_menu
from persistencia import (
    cliente_existe, cargar_cliente, 
    guardar_cliente, listar_numeros_cuenta
)

def crear_nueva_cuenta(numero_cuenta):
    """
    Crea una nueva cuenta de cliente
    
    Args:
        numero_cuenta (str): Número de cuenta para el nuevo cliente
    
    Returns:
        Cliente: Instancia del nuevo cliente creado
    """
    print("\n📝 Creando nueva cuenta...")
    mostrar_titulo("CREACIÓN DE NUEVA CUENTA")
    
    nombre_cl = obtener_texto("Ingrese su nombre: ")
    apellido_cl = obtener_texto("Ingrese su apellido: ")
    balance_inicial = obtener_monto("Ingrese balance inicial (Enter para $0): ")
    
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta, balance_inicial)
    guardar_cliente(cliente)
    
    print("\n✅ ¡Cuenta creada y guardada exitosamente!")
    return cliente


def crear_cliente():
    """
    Crea un nuevo cliente o carga uno existente
    
    Returns:
        Cliente: Instancia del cliente creado o cargado
    """
    print()
    mostrar_titulo("ACCESO AL SISTEMA")
    
    numero_cuenta = obtener_texto("Ingrese su número de cuenta: ")
    
    # Verificar si el cliente ya existe
    if cliente_existe(numero_cuenta):
        print("\n¡Cuenta encontrada! Cargando datos...")
        datos = cargar_cliente(numero_cuenta)
        
        cliente = Cliente(
            datos['nombre'],
            datos['apellido'],
            datos['numero_cuenta'],
            datos['balance']
        )
        cliente.historial = datos.get('historial', [])
        
        print(f"Bienvenido de nuevo, {cliente.nombre} {cliente.apellido}!")
        return cliente
    
# Si no existe, preguntar qué hacer
    print(f"\n⚠️  La cuenta '{numero_cuenta}' no existe en el sistema.")
    print("\n¿Qué desea hacer?")
    print("(C) Crear nueva cuenta")
    print("(V) Volver al inicio")
    
    while True:
        opcion = obtener_texto("\nSeleccione una opción (C/V): ").upper()
        
        if opcion == 'C':
            return crear_nueva_cuenta(numero_cuenta)
        elif opcion == 'V':
            print("\n↩️  Volviendo al inicio...")
            return None
        else:
            print("❌ Opción no válida. Por favor ingrese 'C' para crear o 'V' para volver.")


def procesar_deposito(cliente):
    """Procesa una operación de depósito"""
    monto_dep = obtener_monto("Monto a depositar: $")
    cliente.depositar(monto_dep)



def procesar_deposito(cliente):
    """Procesa una operación de depósito"""
    monto_dep = obtener_monto("Monto a depositar: $")
    cliente.depositar(monto_dep)


def procesar_retiro(cliente):
    """Procesa una operación de retiro"""
    monto_ret = obtener_monto("Monto a retirar: $")
    cliente.retirar(monto_ret)


def procesar_operacion(cliente):
    """
    Procesa la operación seleccionada por el usuario
    
    Args:
        cliente (Cliente): Cliente que realiza la operación
    
    Returns:
        bool: True para continuar, False para salir
    """
    mostrar_menu()
    opcion = obtener_texto("Seleccione una opción: ").upper()

    if opcion == OPCION_DEPOSITAR:
        procesar_deposito(cliente)
    
    elif opcion == OPCION_RETIRAR:
        procesar_retiro(cliente)
    
    elif opcion == OPCION_HISTORIAL:
        cliente.mostrar_historial()
    
    elif opcion == OPCION_SALIR:
        return False
    
    else:
        print("Opción no válida. Por favor intente nuevamente.")
    
    return True
