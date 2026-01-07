"""Módulo de servicios bancarios.
Contiene la lógica de negocio para operaciones bancarias"""

from modelos import Cliente
from utilidades import obtener_monto, obtener_texto, mostrar_titulo, obtener_numero
from constantes import (
    OPCION_DEPOSITAR, OPCION_RETIRAR,
    OPCION_HISTORIAL, OPCION_SALIR,
    OPCION_ELIMINAR
)
from interfaz import mostrar_menu
from persistencia import (
    cliente_existe, cargar_cliente, 
    guardar_cliente, listar_numeros_cuenta,
    eliminar_cliente
)

def crear_nueva_cuenta(numero_cuenta):
    """
    Solicita datos para crear una nueva cuenta y la guarda
    """
    print("\n📝 Creando nueva cuenta...")
    mostrar_titulo("CREACIÓN DE NUEVA CUENTA")
    
    nombre_cl = obtener_texto("Ingrese su nombre: ")
    apellido_cl = obtener_texto("Ingrese su apellido: ")
    balance_inicial = obtener_monto("Ingrese balance inicial (Enter para $0): ")
    
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta, balance_inicial)
    guardar_cliente(cliente)
    
    print("\n✅ ¡Cuenta creada y guardada exitosamente!")

    if numero_cuenta in listar_numeros_cuenta():
        print("Esta cuenta ya existe")
        return cliente

def mostrar_todas_cuentas():
    """Muestra lista de todas las cuentas registradas"""
    cuentas = listar_numeros_cuenta()
    
    if cuentas:
        print("\n" + "="*40)
        print("CUENTAS REGISTRADAS EN EL SISTEMA")
        print("="*40)
        for i, num in enumerate(cuentas, 1):
            print(f"{i}. Cuenta: {num}")
        print("="*40)
    else:
        print("\n⚠️ No hay cuentas registradas en el sistema")



def procesar_eliminacion_cuenta():
    """Elimina una cuenta del sistema"""
    print("\n⚠️  ADVERTENCIA: Esta acción es irreversible")
    
    while True:
        numero_cuenta = input("Ingrese el número de cuenta a eliminar (Enter para cancelar): ").strip()
        
        # Opción para volver sin hacer nada
        if numero_cuenta == "":
            print("🔙 Volviendo al menú...")
            return
        
        # Verificar si la cuenta existe
        if not numero_cuenta.isdigit():
            print("Entrada invalida. Solo se permiten números.")
            continue

        if not cliente_existe(numero_cuenta):
            print(f"\n❌ La cuenta '{numero_cuenta}' no existe.")
            
            # Preguntar si quiere intentar de nuevo
            continuar = obtener_texto("¿Desea intentar con otra cuenta? (S/N): ").upper()
            if continuar != 'S':
                print("🔙 Volviendo al menú...")
                return
            else:
                continue  # Volver a pedir el número de cuenta
        
        # Si la cuenta existe, pedir confirmación
        print(f"\n⚠️  Está por eliminar la cuenta '{numero_cuenta}'")
        confirmacion = obtener_texto("¿Está seguro? (S/N): ").upper()
        
        if confirmacion == 'S':
            if eliminar_cliente(numero_cuenta):
                print(f"\n✅ Cuenta '{numero_cuenta}' eliminada exitosamente")
            else:
                print("\n❌ Error al eliminar la cuenta")
            return True # Salir después de eliminar (exitosa o no)
        else:
            print("\n🔙 Operación cancelada")
            
            # Preguntar si quiere intentar con otra cuenta
            intentar_otra = obtener_texto("¿Desea eliminar otra cuenta? (S/N): ").upper()
            if intentar_otra != 'S':
                print("🔙 Volviendo al menú...")
                return False
            # Si dijo 'S', el while continúa y pide otra cuenta



def busqueda_cliente():
    """Busca un cliente por número de cuenta o crea uno nuevo"""
    print()
    mostrar_titulo("ACCESO AL SISTEMA")

    numero_cuenta = obtener_numero("Ingrese su número de cuenta: ")

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
        if opcion == 'X':
            return eliminar_cliente(numero_cuenta)
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
        
    elif opcion == OPCION_ELIMINAR:
        se_elimino = procesar_eliminacion_cuenta()
        return se_elimino  
    
    elif opcion == OPCION_SALIR:
        return False
    
    else:
        print("Opción no válida. Por favor intente nuevamente.")
    
    return True
