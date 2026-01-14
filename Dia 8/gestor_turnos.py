

# ============================================================================
# ARCHIVO: gestor_turnos.py
# ============================================================================

from typing import Generator, Dict  # Importa type hints
from collections import deque  # Importa cola de doble extremo
from turno import Turno  # Importa clase Turno
from persistencia import GestorPersistencia  # Importa gestor de persistencia


class GestorTurnos:  # Define clase gestora de turnos
    """Gestiona los turnos para las diferentes áreas de la farmacia"""
    
    def __init__(self, archivo_historial: str = 'historial_turnos.json'):  # Constructor
        self.areas = {  # Diccionario con configuración de áreas
            'P': {'nombre': 'Perfumería', 'generador': self._generar_turnos('P'), 'contador': 0},  # Área P
            'F': {'nombre': 'Farmacia', 'generador': self._generar_turnos('F'), 'contador': 0},  # Área F
            'C': {'nombre': 'Cosmética', 'generador': self._generar_turnos('C'), 'contador': 0}  # Área C
        }
        self.turnos_pendientes = {  # Diccionario de colas por área
            'P': deque(),  # Cola vacía para Perfumería
            'F': deque(),  # Cola vacía para Farmacia
            'C': deque()  # Cola vacía para Cosmética
        }
        self.historial = []  # Lista vacía para historial completo
        self.persistencia = GestorPersistencia(archivo_historial)  # Crea instancia de persistencia
        self._restaurar_estado()  # Restaura estado previo desde archivo (nueva modificacion)

    def _restaurar_estado(self):
            """Restaura el estado completo desde el archivo"""
            datos_cargados = self.persistencia.cargar_historial()
            
            if datos_cargados:
                # Restaurar historial
                self.historial = datos_cargados['turnos']
                
                # Restaurar contadores y turnos pendientes
                for area_codigo in self.areas.keys():
                    # Contar turnos emitidos por área
                    turnos_area = [t for t in self.historial if t.numero.startswith(area_codigo)]
                    self.areas[area_codigo]['contador'] = len(turnos_area)
                    
                    # Restaurar turnos pendientes (los que no fueron atendidos)
                    pendientes = [t for t in turnos_area if not t.atendido]
                    self.turnos_pendientes[area_codigo] = deque(pendientes)
                    
                    # Calcular el siguiente número para el generador
                    if turnos_area:
                        # Extraer el último número usado
                        ultimo_numero = max(int(t.numero.split(' - ')[1]) for t in turnos_area)
                        self.areas[area_codigo]['generador'] = self._generar_turnos(area_codigo, inicio=ultimo_numero + 1)
                    else:
                        self.areas[area_codigo]['generador'] = self._generar_turnos(area_codigo, inicio=1)
            else:
                # Si no hay datos previos, inicializar generadores desde 1
                for area_codigo in self.areas.keys():
                    self.areas[area_codigo]['generador'] = self._generar_turnos(area_codigo, inicio=1)


    def _generar_turnos(self, prefijo: str, inicio: int = 1) -> Generator[str, None, None]:  # Generador infinito
        """Generador infinito de números de turno"""
        n = inicio  # Inicializa contador en 1
        while True:  # Bucle infinito
            yield f"{prefijo} - {n}"  # Genera y pausa, retornando turno formateado
            n += 1  # Incrementa contador
    
    def obtener_turno(self, area: str) -> str:  # Método para sacar nuevo turno
        """Obtiene el siguiente turno para el área especificada"""
        if area not in self.areas:  # Verifica si área existe
            raise ValueError(f"Área '{area}' no válida")  # Lanza excepción si no existe
        
        numero_turno = next(self.areas[area]['generador'])  # Obtiene siguiente número del generador
        turno = Turno(numero_turno, self.areas[area]['nombre'])  # Crea objeto Turno
        
        self.turnos_pendientes[area].append(turno)  # Agrega turno a cola del área
        self.historial.append(turno)  # Agrega turno al historial
        self.areas[area]['contador'] += 1  # Incrementa contador de área
        
        self.persistencia.guardar_historial(self.historial)  # Guarda historial en archivo
        
        # Presentación del turno (antes era parte del decorador)
        print("\n" + "=" * 40)
        print("Su número es:")
        print(f"  >>> {numero_turno} <<<")
        print("Aguarde y será atendido")
        print("=" * 40 + "\n")

        return numero_turno  # Retorna número de turno
    
    def llamar_turno(self, area: str) -> Turno:  # Método para atender turno
        """Llama al siguiente turno en espera del área especificada"""
        if area not in self.areas:  # Valida que área exista
            raise ValueError(f"Área '{area}' no válida")  # Lanza error si no existe
        
        if not self.turnos_pendientes[area]:  # Verifica si hay turnos en cola
            raise ValueError(f"No hay turnos pendientes en {self.areas[area]['nombre']}")  # Error si vacía
        
        turno = self.turnos_pendientes[area].popleft()  # Extrae primer turno de la cola (FIFO)
        turno.marcar_atendido()  # Marca turno como atendido
        self.persistencia.guardar_historial(self.historial)  # Guarda cambios
        return turno  # Retorna turno atendido
    
    def mostrar_turnos_pendientes(self):  # Método para mostrar turnos en espera
        """Muestra todos los turnos pendientes por área"""
        print("\n" + "=" * 40)  # Imprime línea superior
        print("TURNOS EN ESPERA:")  # Título
        print("=" * 40)  # Línea decorativa
        hay_turnos = False  # Bandera para verificar si hay turnos
        
        for codigo, info in self.areas.items():  # Itera sobre áreas
            pendientes = list(self.turnos_pendientes[codigo])  # Convierte deque a lista
            if pendientes:  # Si hay turnos pendientes
                hay_turnos = True  # Marca bandera como verdadera
                print(f"\n{info['nombre']}:")  # Imprime nombre del área
                for turno in pendientes:  # Itera sobre turnos pendientes
                    print(f"  • {turno.numero}")  # Imprime número de turno
        
        if not hay_turnos:  # Si no hay turnos
            print("  No hay turnos pendientes")  # Mensaje informativo
        print("=" * 40 + "\n")  # Línea de cierre
    
    def mostrar_estadisticas(self):  # Método para mostrar estadísticas
        """Muestra estadísticas de turnos emitidos"""
        print("\n" + "-" * 40)  # Línea superior
        print("ESTADÍSTICAS DE TURNOS:")  # Título
        print("-" * 40)  # Línea decorativa
        for codigo, info in self.areas.items():  # Itera sobre áreas
            pendientes = len(self.turnos_pendientes[codigo])  # Cuenta turnos pendientes
            print(f"{info['nombre']:15} | Emitidos: {info['contador']} | En espera: {pendientes}")  # Muestra datos
        print(f"\nTotal en historial: {len(self.historial)}")  # Muestra total del historial
        print("-" * 40 + "\n")  # Línea de cierre
    
    def obtener_areas_disponibles(self) -> Dict[str, str]:  # Método que retorna diccionario de áreas
        """Retorna las áreas disponibles"""
        return {k: v['nombre'] for k, v in self.areas.items()}  # Comprensión de diccionario

