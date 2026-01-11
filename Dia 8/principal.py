from gestor_turnos import GestorTurnos
from interfaz import InterfazUsuario


class FarmaciaApp:
    """Aplicación principal del sistema de turnos"""
    
    def __init__(self):
        self.gestor = GestorTurnos()
        self.interfaz = InterfazUsuario()
        self.ejecutando = True
    
    def procesar_opcion(self, opcion: str):
        """Procesa la opción seleccionada por el usuario"""
        
        if opcion == 'S':
            self.ejecutando = False
            self.interfaz.mostrar_despedida()
        
        elif opcion == 'E':
            self.gestor.mostrar_estadisticas()
        
        elif opcion == 'T':
            self.gestor.mostrar_turnos_pendientes()
        
        elif opcion in ['1', '2', '3']:
            self._llamar_turno(opcion)
        
        else:
            self._sacar_turno(opcion)
    
    def _llamar_turno(self, opcion: str):
        """Llama a un turno del área especificada"""
        mapa_areas = {'1': 'P', '2': 'F', '3': 'C'}
        area = mapa_areas[opcion]
        try:
            turno = self.gestor.llamar_turno(area)
            self.interfaz.mostrar_llamada_turno(turno)
        except ValueError as e:
            print(f"\n❌ {e}\n")
    
    def _sacar_turno(self, area: str):
        """Saca un nuevo turno para el área especificada"""
        try:
            self.gestor.obtener_turno(area)
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    def ejecutar(self):
        """Ejecuta el ciclo principal de la aplicación"""
        while self.ejecutando:
            areas = self.gestor.obtener_areas_disponibles()
            self.interfaz.mostrar_menu(areas)
            
            opciones_validas = list(areas.keys()) + ['1', '2', '3', 'T', 'E', 'S']
            opcion = self.interfaz.solicitar_opcion("Elija su opción: ", opciones_validas)
            
            self.procesar_opcion(opcion)
