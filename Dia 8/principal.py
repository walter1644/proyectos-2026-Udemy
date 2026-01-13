
# ============================================================================
# ARCHIVO: principal.py
# ============================================================================

from gestor_turnos import GestorTurnos  # Importa gestor de turnos
from interfaz import InterfazUsuario  # Importa interfaz de usuario


class FarmaciaApp:  # Define clase principal de la aplicación
    """Aplicación principal del sistema de turnos"""
    
    def __init__(self):  # Constructor
        self.gestor = GestorTurnos()  # Crea instancia de gestor
        self.interfaz = InterfazUsuario()  # Crea instancia de interfaz
        self.ejecutando = True  # Bandera para controlar bucle principal
    
    def procesar_opcion(self, opcion: str):  # Método que procesa opción elegida
        """Procesa la opción seleccionada por el usuario"""
        
        if opcion == 'S':  # Si opción es salir
            self.ejecutando = False  # Cambia bandera a False
            self.interfaz.mostrar_despedida()  # Muestra despedida
        
        elif opcion == 'E':  # Si opción es estadísticas
            self.gestor.mostrar_estadisticas()  # Muestra estadísticas
            input("\n👉 Presione ENTER para continuar...")  # Pausa
        
        elif opcion == 'T':  # Si opción es ver turnos
            self.gestor.mostrar_turnos_pendientes()  # Muestra turnos pendientes
            input("\n👉 Presione ENTER para continuar...")  # Pausa

        elif opcion in ['1', '2', '3']:  # Si opción es llamar turno
            self._llamar_turno(opcion)  # Llama método privado
        
        else:  # Si opción es área (P, F, C)
            self._sacar_turno(opcion)  # Saca nuevo turno
    
    def _llamar_turno(self, opcion: str):  # Método privado para llamar turno
        """Llama a un turno del área especificada"""
        mapa_areas = {'1': 'P', '2': 'F', '3': 'C'}  # Mapeo de número a código de área
        area = mapa_areas[opcion]  # Obtiene código de área
        try:  # Intenta ejecutar
            turno = self.gestor.llamar_turno(area)  # Llama turno del área
            self.interfaz.mostrar_llamada_turno(turno)  # Muestra mensaje de llamada
            input("\n👉 Presione ENTER para continuar...")  # Pausa
        except ValueError as e:  # Captura error de valor
            print(f"\n❌ {e}\n")  # Muestra mensaje de error
            input("\n👉 Presione ENTER para continuar...")  # Pausa
    
    def _sacar_turno(self, area: str):  # Método privado para sacar turno
        """Saca un nuevo turno para el área especificada"""
        try:  # Intenta ejecutar
            self.gestor.obtener_turno(area)  # Obtiene nuevo turno
            input("\n👉 Presione ENTER para continuar...")  # Pausa
        except ValueError as e:  # Captura error
            print(f"❌ Error: {e}")  # Muestra error
    
    def ejecutar(self):  # Método principal que ejecuta aplicación
        """Ejecuta el ciclo principal de la aplicación"""
        while self.ejecutando:  # Mientras bandera sea True
            areas = self.gestor.obtener_areas_disponibles()  # Obtiene áreas disponibles
            self.interfaz.mostrar_menu(areas)  # Muestra menú
            
            opciones_validas = list(areas.keys()) + ['1', '2', '3', 'T', 'E', 'S']  # Lista de opciones válidas
            opcion = self.interfaz.solicitar_opcion("Elija su opción: ", opciones_validas)  # Solicita opción
            
            self.procesar_opcion(opcion)  # Procesa opción elegida
