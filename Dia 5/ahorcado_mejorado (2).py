# ===== ARCHIVO: models.py =====
# Contiene las clases y estructuras de datos del juego

class EstadoJuego:
    """Representa el estado actual de una partida"""
    
    def __init__(self, palabra, letras_unicas):
        self.palabra = palabra
        self.letras_unicas = letras_unicas
        self.letras_correctas = []
        self.letras_incorrectas = []
        self.intentos = 6
        self.aciertos = 0
        self.juego_terminado = False
        self.pistas_usadas = 0
    
    def reiniciar(self, palabra, letras_unicas):
        """Reinicia el estado para una nueva partida"""
        self.__init__(palabra, letras_unicas)


class Estadisticas:
    """Maneja las estadísticas del jugador"""
    
    def __init__(self):
        self.partidas_jugadas = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0
        self.racha_actual = 0
        self.mejor_racha = 0
    
    def registrar_victoria(self):
        """Registra una victoria"""
        self.partidas_jugadas += 1
        self.partidas_ganadas += 1
        self.racha_actual += 1
        if self.racha_actual > self.mejor_racha:
            self.mejor_racha = self.racha_actual
    
    def registrar_derrota(self):
        """Registra una derrota"""
        self.partidas_jugadas += 1
        self.partidas_perdidas += 1
        self.racha_actual = 0
    
    def to_dict(self):
        """Convierte las estadísticas a diccionario"""
        return {
            'partidas_jugadas': self.partidas_jugadas,
            'partidas_ganadas': self.partidas_ganadas,
            'partidas_perdidas': self.partidas_perdidas,
            'racha_actual': self.racha_actual,
            'mejor_racha': self.mejor_racha
        }
    
    def from_dict(self, datos):
        """Carga las estadísticas desde un diccionario"""
        self.partidas_jugadas = datos.get('partidas_jugadas', 0)
        self.partidas_ganadas = datos.get('partidas_ganadas', 0)
        self.partidas_perdidas = datos.get('partidas_perdidas', 0)
        self.racha_actual = datos.get('racha_actual', 0)
        self.mejor_racha = datos.get('mejor_racha', 0)


# ===== ARCHIVO: palabras.py =====
# Contiene las listas de palabras y lógica para seleccionarlas

from random import choice

PALABRAS_FACIL = ['gato', 'perro', 'casa', 'mesa', 'libro', 'agua', 'sol', 'luna']
PALABRAS_MEDIO = ['panadero', 'tiburon', 'guitarra', 'ventana', 'computadora', 'elefante']
PALABRAS_DIFICIL = ['dinosaurio', 'helipuerto', 'arquitectura', 'filosofia', 'hipopotamo', 'ornitorrinco']


class GestorPalabras:
    """Gestiona la selección y seguimiento de palabras"""
    
    def __init__(self):
        self.palabras_jugadas = []
    
    def obtener_palabras_por_dificultad(self, dificultad):
        """Retorna la lista de palabras según la dificultad"""
        if dificultad == 'facil':
            return PALABRAS_FACIL
        elif dificultad == 'medio':
            return PALABRAS_MEDIO
        elif dificultad == 'dificil':
            return PALABRAS_DIFICIL
        return PALABRAS_MEDIO
    
    def elegir_palabra(self, lista_palabras):
        """Elige una palabra al azar que no se haya jugado"""
        palabras_disponibles = [p for p in lista_palabras if p not in self.palabras_jugadas]
        
        if not palabras_disponibles:
            self.palabras_jugadas.clear()
            palabras_disponibles = lista_palabras
        
        palabra_elegida = choice(palabras_disponibles)
        self.palabras_jugadas.append(palabra_elegida)
        letras_unicas = len(set(palabra_elegida))
        
        return palabra_elegida, letras_unicas
    
    def reiniciar_historial(self):
        """Limpia el historial de palabras jugadas"""
        self.palabras_jugadas.clear()


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


# ===== ARCHIVO: vista.py =====
# Maneja toda la interfaz de usuario y visualización

class Vista:
    """Maneja toda la presentación visual del juego"""
    
    @staticmethod
    def mostrar_ahorcado(vidas):
        """Dibuja el ahorcado según las vidas restantes"""
        estados = [
            # 0 vidas
            '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ---------
            ''',
            # 1 vida
            '''
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        ---------
            ''',
            # 2 vidas
            '''
           -----
           |   |
           |   O
           |  /|\\
           |
           |
        ---------
            ''',
            # 3 vidas
            '''
           -----
           |   |
           |   O
           |  /|
           |
           |
        ---------
            ''',
            # 4 vidas
            '''
           -----
           |   |
           |   O
           |   |
           |
           |
        ---------
            ''',
            # 5 vidas
            '''
           -----
           |   |
           |   O
           |
           |
           |
        ---------
            ''',
            # 6 vidas
            '''
           -----
           |   |
           |
           |
           |
           |
        ---------
            '''
        ]
        print(estados[vidas])
    
    @staticmethod
    def mostrar_tablero(palabra, letras_correctas):
        """Muestra el estado actual de la palabra"""
        lista_oculta = []
        for letra in palabra:
            if letra in letras_correctas:
                lista_oculta.append(letra)
            else:
                lista_oculta.append('-')
        print(' '.join(lista_oculta))
    
    @staticmethod
    def mostrar_estado_juego(estado):
        """Muestra el estado completo del juego"""
        print('\n' + '*' * 40 + '\n')
        Vista.mostrar_ahorcado(estado.intentos)
        Vista.mostrar_tablero(estado.palabra, estado.letras_correctas)
        print('\n')
        if estado.letras_incorrectas:
            print('Letras incorrectas: ' + ' '.join(estado.letras_incorrectas))
        else:
            print('Letras incorrectas: Ninguna')
        print(f'Vidas: {estado.intentos}')
        print(f'Pistas usadas: {estado.pistas_usadas}')
        print('\n' + '*' * 40 + '\n')
    
    @staticmethod
    def mostrar_menu_principal():
        """Muestra el menú principal"""
        print('\n' + '=' * 40)
        print('JUEGO DEL AHORCADO')
        print('=' * 40)
        print('1. Jugar')
        print('2. Instrucciones')
        print('3. Ver estadísticas')
        print('4. Salir')
        print('=' * 40)
    
    @staticmethod
    def mostrar_menu_dificultad():
        """Muestra el menú de dificultad"""
        print('\n--- SELECCIONA LA DIFICULTAD ---')
        print('1. Fácil (4-5 letras)')
        print('2. Medio (6-8 letras)')
        print('3. Difícil (9+ letras)')
    
    @staticmethod
    def mostrar_menu_accion():
        """Muestra el menú de acciones durante el juego"""
        print('¿Qué deseas hacer?')
        print('1. Elegir una letra')
        print('2. Usar una pista (cuesta 1 vida)')
    
    @staticmethod
    def mostrar_instrucciones():
        """Muestra las instrucciones del juego"""
        print('\n' + '=' * 40)
        print('INSTRUCCIONES DEL AHORCADO')
        print('=' * 40)
        print('1. El juego elige una palabra secreta')
        print('2. Debes adivinar la palabra letra por letra')
        print('3. Tienes 6 vidas')
        print('4. Cada letra incorrecta te resta una vida')
        print('5. Puedes usar pistas (te cuestan una vida)')
        print('6. Ganas si adivinas antes de perder todas las vidas')
        print('=' * 40 + '\n')
    
    @staticmethod
    def mostrar_estadisticas(estadisticas):
        """Muestra las estadísticas del jugador"""
        print('\n' + '=' * 40)
        print('ESTADÍSTICAS')
        print('=' * 40)
        print(f'Partidas jugadas: {estadisticas.partidas_jugadas}')
        print(f'Partidas ganadas: {estadisticas.partidas_ganadas}')
        print(f'Partidas perdidas: {estadisticas.partidas_perdidas}')
        if estadisticas.partidas_jugadas > 0:
            porcentaje = (estadisticas.partidas_ganadas / estadisticas.partidas_jugadas) * 100
            print(f'Porcentaje de victorias: {porcentaje:.1f}%')
        print(f'Racha actual: {estadisticas.racha_actual}')
        print(f'Mejor racha: {estadisticas.mejor_racha}')
        print('=' * 40 + '\n')
    
    @staticmethod
    def mostrar_victoria(palabra, puntuacion, vidas_restantes, pistas_usadas):
        """Muestra el mensaje de victoria"""
        print("\n" + "=" * 40)
        print("¡FELICITACIONES!")
        print("=" * 40)
        print(f'\n¡Has encontrado la palabra: "{palabra.upper()}"!')
        print(f'Tu puntuación: {puntuacion} puntos')
        print(f'Vidas restantes: {vidas_restantes}')
        print(f'Pistas usadas: {pistas_usadas}')
    
    @staticmethod
    def mostrar_derrota(palabra):
        """Muestra el mensaje de derrota"""
        print("\n" + "=" * 40)
        print("¡GAME OVER!")
        print("=" * 40)
        Vista.mostrar_ahorcado(0)
        print(f"Te has quedado sin vidas.")
        print(f'La palabra oculta era: "{palabra.upper()}"')
    
    @staticmethod
    def mostrar_pista(letra):
        """Muestra el mensaje de pista"""
        print(f'\n¡PISTA! La letra "{letra}" está en la palabra.')
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        """Muestra un mensaje genérico"""
        print(mensaje)


# ===== ARCHIVO: entrada.py =====
# Maneja toda la entrada del usuario

class GestorEntrada:
    """Maneja las entradas del usuario"""
    
    @staticmethod
    def obtener_opcion_menu():
        """Obtiene la opción del menú principal"""
        return input('Elige una opción: ')
    
    @staticmethod
    def obtener_dificultad():
        """Obtiene la dificultad elegida por el usuario"""
        return input('Elige una opción (1-3): ')
    
    @staticmethod
    def obtener_letra(letras_usadas):
        """Solicita una letra al jugador"""
        abecedario = 'abcdefghijklmnñopqrstuvwxyz'
        
        while True:
            letra = input("Elige una letra: ").lower()
            
            if letra in letras_usadas:
                print("Ya has usado esa letra. Intenta con otra.")
            elif letra in abecedario and len(letra) == 1:
                return letra
            else:
                print("No has elegido una letra correcta")
    
    @staticmethod
    def obtener_accion():
        """Obtiene la acción del usuario durante el juego"""
        return input('Elige (1 o 2): ')
    
    @staticmethod
    def obtener_confirmacion(mensaje):
        """Obtiene una confirmación sí/no del usuario"""
        while True:
            respuesta = input(mensaje).lower()
            if respuesta == 's':
                return True
            elif respuesta == 'n':
                return False
            else:
                print('Por favor responde "s" para sí o "n" para no.')


# ===== ARCHIVO: logica_juego.py =====
# Contiene la lógica principal del juego

from random import choice


class LogicaJuego:
    """Maneja toda la lógica del juego"""
    
    @staticmethod
    def verificar_letra(letra, estado):
        """Verifica si la letra está en la palabra y actualiza el estado"""
        if letra in estado.palabra:
            estado.letras_correctas.append(letra)
            estado.aciertos += 1
            return True
        else:
            estado.letras_incorrectas.append(letra)
            estado.intentos -= 1
            return False
    
    @staticmethod
    def verificar_victoria(estado):
        """Verifica si el jugador ha ganado"""
        return estado.aciertos == estado.letras_unicas
    
    @staticmethod
    def verificar_derrota(estado):
        """Verifica si el jugador ha perdido"""
        return estado.intentos == 0
    
    @staticmethod
    def usar_pista(estado):
        """Usa una pista revelando una letra aleatoria"""
        letras_ocultas = [l for l in set(estado.palabra) if l not in estado.letras_correctas]
        
        if letras_ocultas:
            letra_revelada = choice(letras_ocultas)
            estado.letras_correctas.append(letra_revelada)
            estado.pistas_usadas += 1
            estado.intentos -= 1
            estado.aciertos = sum(1 for l in set(estado.palabra) if l in estado.letras_correctas)
            return letra_revelada
        return None
    
    @staticmethod
    def calcular_puntuacion(estado):
        """Calcula la puntuación final"""
        puntos_base = 100
        puntos_por_vida = estado.intentos * 20
        puntos_por_dificultad = len(estado.palabra) * 10
        penalizacion_pistas = estado.pistas_usadas * 30
        
        puntuacion_total = puntos_base + puntos_por_vida + puntos_por_dificultad - penalizacion_pistas
        return max(puntuacion_total, 0)


# ===== ARCHIVO: controlador.py =====
# Coordina todos los módulos

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


# ===== ARCHIVO: main.py =====
# Punto de entrada del programa

def main():
    """Función principal que inicializa y ejecuta el juego"""
    # Inicializar componentes
    vista = Vista()
    gestor_entrada = GestorEntrada()
    gestor_palabras = GestorPalabras()
    gestor_persistencia = GestorPersistencia()
    
    # Cargar estadísticas
    estadisticas = Estadisticas()
    datos_guardados = gestor_persistencia.cargar_estadisticas()
    if datos_guardados:
        estadisticas.from_dict(datos_guardados)
    
    # Crear controlador y ejecutar
    controlador = ControladorJuego(
        vista,
        gestor_entrada,
        gestor_palabras,
        gestor_persistencia,
        estadisticas
    )
    
    controlador.ejecutar()


if __name__ == "__main__":
    main()