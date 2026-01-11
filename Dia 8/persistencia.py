import json
from datetime import datetime
from typing import List
from turno import Turno


class GestorPersistencia:
    """Maneja el guardado y carga de turnos en archivo JSON"""
    
    def __init__(self, archivo: str = 'historial_turnos.json'):
        self.archivo = archivo
    
    def guardar_historial(self, turnos: List[Turno]):
        """Guarda el historial de turnos en archivo JSON"""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                datos = {
                    'turnos': [turno.to_dict() for turno in turnos],
                    'ultima_actualizacion': datetime.now().isoformat()
                }
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Error al guardar historial: {e}")
    
    def cargar_historial(self) -> int:
        """Carga el historial de turnos desde archivo JSON"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                cantidad = len(datos.get('turnos', []))
                print(f"✅ Historial cargado: {cantidad} turnos registrados")
                return cantidad
        except FileNotFoundError:
            print("📝 Creando nuevo historial de turnos...")
            return 0
        except Exception as e:
            print(f"⚠️  Error al cargar historial: {e}")
            return 0
