

# ============================================================================
# ARCHIVO: persistencia.py
# ============================================================================

import json  # Importa módulo para trabajar con JSON
from datetime import datetime  # Importa clase datetime
from typing import List  # Importa type hint para listas
from turno import Turno  # Importa clase Turno


class GestorPersistencia:  # Define clase para manejar persistencia
    """Maneja el guardado y carga de turnos en archivo JSON"""
    
    def __init__(self, archivo: str = 'historial_turnos.json'):  # Constructor con archivo por defecto
        self.archivo = archivo  # Guarda nombre del archivo
    
    def guardar_historial(self, turnos: List[Turno]):  # Método que guarda lista de turnos
        """Guarda el historial de turnos en archivo JSON"""
        try:  # Intenta ejecutar bloque de código
            with open(self.archivo, 'w', encoding='utf-8') as f:  # Abre archivo en modo escritura
                datos = {  # Crea diccionario con datos a guardar
                    'turnos': [turno.serializar() for turno in turnos],  # Lista de turnos serializados
                    'ultima_actualizacion': datetime.now().strftime("%d/%m/%Y %H:%M")  # Fecha actual
                }
                json.dump(datos, f, indent=2, ensure_ascii=False)  # Guarda JSON con formato legible
        except Exception as e:  # Captura cualquier error
            print(f"⚠️ Error al guardar historial: {e}")  # Muestra mensaje de error
    
    def cargar_historial(self) -> int:  # Método que carga historial y retorna cantidad
        """Carga el historial de turnos desde archivo JSON"""
        try:  # Intenta ejecutar bloque
            with open(self.archivo, 'r', encoding='utf-8') as f:  # Abre archivo en modo lectura
                datos = json.load(f)  # Carga y parsea JSON
                turnos_serializados = datos.get('turnos', [])
                
                # Convertir datos JSON a objetos Turno
                turnos = []
                for t_data in turnos_serializados:
                    turno = Turno.deserializar(t_data)
                    turnos.append(turno)
                
                cantidad = len(datos.get('turnos', []))  # Cuenta turnos o usa lista vacía
                print(f"✅ Historial cargado: {cantidad} turnos registrados")  # Mensaje de éxito
                return {
                    'turnos': turnos,
                    'ultima_actualizacion': datos.get('ultima_actualizacion')
                }
            
        except FileNotFoundError:  # Captura error si archivo no existe
            print("📝 Creando nuevo historial de turnos...")  # Mensaje informativo
            return 0  # Retorna cero turnos
        except Exception as e:  # Captura otros errores
            print(f"⚠️ Error al cargar historial: {e}")  # Mensaje de error
            return 0  # Retorna cero
