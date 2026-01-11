from typing import Generator, Dict
from collections import deque
from turno import Turno
from decoradores import decorador_turno
from persistencia import GestorPersistencia


class GestorTurnos:
    """Gestiona los turnos para las diferentes áreas de la farmacia"""
    
    def __init__(self, archivo_historial: str = 'historial_turnos.json'):
        self.areas = {
            'P': {'nombre': 'Perfumería', 'generador': self._generar_turnos('P'), 'contador': 0},
            'F': {'nombre': 'Farmacia', 'generador': self._generar_turnos('F'), 'contador': 0},
            'C': {'nombre': 'Cosmética', 'generador': self._generar_turnos('C'), 'contador': 0}
        }
        self.turnos_pendientes = {
            'P': deque(),
            'F': deque(),
            'C': deque()
        }
        self.historial = []
        self.persistencia = GestorPersistencia(archivo_historial)
        self.persistencia.cargar_historial()
    
    def _generar_turnos(self, prefijo: str) -> Generator[str, None, None]:
        """Generador infinito de números de turno"""
        n = 1
        while True:
            yield f"{prefijo} - {n}"
            n += 1
    
    @decorador_turno
    def obtener_turno(self, area: str) -> str:
        """Obtiene el siguiente turno para el área especificada"""
        if area not in self.areas:
            raise ValueError(f"Área '{area}' no válida")
        
        numero_turno = next(self.areas[area]['generador'])
        turno = Turno(numero_turno, self.areas[area]['nombre'])
        
        self.turnos_pendientes[area].append(turno)
        self.historial.append(turno)
        self.areas[area]['contador'] += 1
        
        self.persistencia.guardar_historial(self.historial)
        return numero_turno
    
    def llamar_turno(self, area: str) -> Turno:
        """Llama al siguiente turno en espera del área especificada"""
        if area not in self.areas:
            raise ValueError(f"Área '{area}' no válida")
        
        if not self.turnos_pendientes[area]:
            raise ValueError(f"No hay turnos pendientes en {self.areas[area]['nombre']}")
        
        turno = self.turnos_pendientes[area].popleft()
        turno.marcar_atendido()
        self.persistencia.guardar_historial(self.historial)
        return turno
    
    def mostrar_turnos_pendientes(self):
        """Muestra todos los turnos pendientes por área"""
        print("\n" + "=" * 40)
        print("TURNOS EN ESPERA:")
        print("=" * 40)
        hay_turnos = False
        
        for codigo, info in self.areas.items():
            pendientes = list(self.turnos_pendientes[codigo])
            if pendientes:
                hay_turnos = True
                print(f"\n{info['nombre']}:")
                for turno in pendientes:
                    print(f"  • {turno.numero}")
        
        if not hay_turnos:
            print("  No hay turnos pendientes")
        print("=" * 40 + "\n")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de turnos emitidos"""
        print("\n" + "-" * 40)
        print("ESTADÍSTICAS DE TURNOS:")
        print("-" * 40)
        for codigo, info in self.areas.items():
            pendientes = len(self.turnos_pendientes[codigo])
            print(f"{info['nombre']:15} | Emitidos: {info['contador']} | En espera: {pendientes}")
        print(f"\nTotal en historial: {len(self.historial)}")
        print("-" * 40 + "\n")
    
    def obtener_areas_disponibles(self) -> Dict[str, str]:
        """Retorna las áreas disponibles"""
        return {k: v['nombre'] for k, v in self.areas.items()}
