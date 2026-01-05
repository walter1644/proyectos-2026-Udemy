# ==================== persistencia.py ====================
"""
Módulo de persistencia de datos
Guarda y carga la información de clientes en archivos JSON
"""
import json
import os
from datetime import datetime


ARCHIVO_CLIENTES = "clientes_banco.json"


def guardar_cliente(cliente):
    """
    Guarda la información del cliente en un archivo JSON
    
    Args:
        cliente (Cliente): Cliente a guardar
    
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    try:
        # Leer clientes existentes
        clientes_guardados = cargar_todos_clientes()
        
        # Convertir el cliente a diccionario
        cliente_dict = {
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'numero_cuenta': cliente.numero_cuenta,
            'balance': cliente.balance,
            'historial': cliente.historial,
            'ultima_actualizacion': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Actualizar o agregar el cliente
        clientes_guardados[cliente.numero_cuenta] = cliente_dict
        
        # Guardar en el archivo
        with open(ARCHIVO_CLIENTES, 'w', encoding='utf-8') as archivo:
            json.dump(clientes_guardados, archivo, indent=4, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"Error al guardar cliente: {e}")
        return False


def cargar_cliente(numero_cuenta):
    """
    Carga un cliente específico desde el archivo JSON
    
    Args:
        numero_cuenta (str): Número de cuenta del cliente
    
    Returns:
        dict: Datos del cliente o None si no existe
    """
    try:
        clientes = cargar_todos_clientes()
        return clientes.get(numero_cuenta)
    
    except Exception as e:
        print(f"Error al cargar cliente: {e}")
        return None


def cargar_todos_clientes():
    """
    Carga todos los clientes guardados
    
    Returns:
        dict: Diccionario con todos los clientes (clave: número de cuenta)
    """
    if not os.path.exists(ARCHIVO_CLIENTES):
        return {}
    
    try:
        with open(ARCHIVO_CLIENTES, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    
    except Exception as e:
        print(f"Error al cargar clientes: {e}")
        return {}


def cliente_existe(numero_cuenta):
    """
    Verifica si un cliente existe en el sistema
    
    Args:
        numero_cuenta (str): Número de cuenta a verificar
    
    Returns:
        bool: True si existe, False si no
    """
    clientes = cargar_todos_clientes()
    return numero_cuenta in clientes


def listar_numeros_cuenta():
    """
    Lista todos los números de cuenta guardados
    
    Returns:
        list: Lista de números de cuenta
    """
    clientes = cargar_todos_clientes()
    return list(clientes.keys())


def eliminar_cliente(numero_cuenta):
    """
    Elimina un cliente del sistema
    
    Args:
        numero_cuenta (str): Número de cuenta a eliminar
    
    Returns:
        bool: True si se eliminó, False si no
    """
    try:
        clientes = cargar_todos_clientes()
        
        if numero_cuenta in clientes:
            del clientes[numero_cuenta]
            
            with open(ARCHIVO_CLIENTES, 'w', encoding='utf-8') as archivo:
                json.dump(clientes, archivo, indent=4, ensure_ascii=False)
            
            return True
        
        return False
    
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")
        return False
