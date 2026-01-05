# ===== ARCHIVO: controlador.py =====
# Coordina todos los módulos

from models import EstadoJuego
from logica_juego import LogicaJuego

class ControladorJuego:
    """Controlador principal que coordina todos los módulos"""
    
    def __init__(self, vista, gestor_entrada, gestor_palabras, gestor_persistencia, estadisticas):
        self.vista = vista
        self.entrada = gestor_entrada
        self.palabras = gestor_palabras
        self.persistencia = gestor_persistencia
        self.estadisticas = estadisticas
        self.logica = LogicaJuego()
    
    def ejecutar(self):
        """Ejecuta el programa principal"""
        while True:
            accion = self._mostrar_menu_principal()
            
            if accion == 'salir':
                break
            elif accion == 'jugar':
                self._jugar_partida()
                self._preguntar_jugar_de_nuevo()
    
    def _mostrar_menu_principal(self):
        """Muestra el menú principal y procesa la opción"""
        while True:
            self.vista.mostrar_menu_principal()
            opcion = self.entrada.obtener_opcion_menu()
            
            if opcion == '1':
                return 'jugar'
            elif opcion == '2':
                self.vista.mostrar_instrucciones()
            elif opcion == '3':
                self.vista.mostrar_estadisticas(self.estadisticas)
            elif opcion == '4':
                self.vista.mostrar_mensaje('\n¡Gracias por jugar! Hasta pronto.')
                return 'salir'
            else:
                self.vista.mostrar_mensaje('Opción no válida. Intenta de nuevo.')
    
    def _elegir_dificultad(self):
        """Permite elegir la dificultad"""
        while True:
            self.vista.mostrar_menu_dificultad()
            opcion = self.entrada.obtener_dificultad()
            
            if opcion == '1':
                return 'facil'
            elif opcion == '2':
                return 'medio'
            elif opcion == '3':
                return 'dificil'
            else:
                self.vista.mostrar_mensaje('Opción no válida. Intenta de nuevo.')
    
    def _jugar_partida(self):
        """Ejecuta una partida completa"""
        dificultad = self._elegir_dificultad()
        lista_palabras = self.palabras.obtener_palabras_por_dificultad(dificultad)
        palabra, letras_unicas = self.palabras.elegir_palabra(lista_palabras)
        
        estado = EstadoJuego(palabra, letras_unicas)
        
        while not estado.juego_terminado:
            self.vista.mostrar_estado_juego(estado)
            self.vista.mostrar_menu_accion()
            accion = self.entrada.obtener_accion()
            
            if accion == '2' and estado.intentos > 1:
                self._procesar_pista(estado)
            elif accion == '1':
                self._procesar_letra(estado)
            else:
                self.vista.mostrar_mensaje('Opción no válida o no tienes suficientes vidas para una pista.')
    
    def _procesar_letra(self, estado):
        """Procesa la entrada de una letra"""
        letras_usadas = estado.letras_correctas + estado.letras_incorrectas
        letra = self.entrada.obtener_letra(letras_usadas)
        
        self.logica.verificar_letra(letra, estado)
        
        if self.logica.verificar_victoria(estado):
            self._finalizar_victoria(estado)
        elif self.logica.verificar_derrota(estado):
            self._finalizar_derrota(estado)
    
    def _procesar_pista(self, estado):
        """Procesa el uso de una pista"""
        letra_revelada = self.logica.usar_pista(estado)
        if letra_revelada:
            self.vista.mostrar_pista(letra_revelada)
            if self.logica.verificar_victoria(estado):
                self._finalizar_victoria(estado)
    
    def _finalizar_victoria(self, estado):
        """Finaliza el juego con victoria"""
        puntuacion = self.logica.calcular_puntuacion(estado)
        self.vista.mostrar_tablero(estado.palabra, estado.letras_correctas)
        self.vista.mostrar_victoria(estado.palabra, puntuacion, estado.intentos, estado.pistas_usadas)
        self.estadisticas.registrar_victoria()
        self.persistencia.guardar_estadisticas(self.estadisticas.to_dict())
        estado.juego_terminado = True
    
    def _finalizar_derrota(self, estado):
        """Finaliza el juego con derrota"""
        self.vista.mostrar_derrota(estado.palabra)
        self.estadisticas.registrar_derrota()
        self.persistencia.guardar_estadisticas(self.estadisticas.to_dict())
        estado.juego_terminado = True
    
    def _preguntar_jugar_de_nuevo(self):
        """Pregunta si quiere jugar de nuevo"""
        while self.entrada.obtener_confirmacion('\n¿Quieres jugar de nuevo? (s/n): '):
            self._jugar_partida()