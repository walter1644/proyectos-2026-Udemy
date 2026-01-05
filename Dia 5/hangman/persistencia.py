# ===== ARCHIVO: persistencia.py =====
# Maneja la carga y guardado de datos

import json
import os


class GestorPersistencia:
    """Maneja la persistencia de datos en archivos"""
    
    def __init__(self, archivo='estadisticas_ahorcado.json'):
        self.archivo = archivo
    
    def cargar_estadisticas(self):
        """Carga las estadísticas desde un archivo JSON"""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    return json.load(f)
            except:
                pass
        return None
    
    def guardar_estadisticas(self, estadisticas_dict):
        """Guarda las estadísticas en un archivo JSON"""
        with open(self.archivo, 'w') as f:
            json.dump(estadisticas_dict, f, indent=2)