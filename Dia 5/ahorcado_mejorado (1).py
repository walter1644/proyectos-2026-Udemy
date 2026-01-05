from random import choice
import json
import os

# Palabras categorizadas por dificultad
PALABRAS_FACIL = ['gato', 'perro', 'casa', 'mesa', 'libro', 'agua', 'sol', 'luna']
PALABRAS_MEDIO = ['panadero', 'tiburon', 'guitarra', 'ventana', 'computadora', 'elefante']
PALABRAS_DIFICIL = ['dinosaurio', 'helipuerto', 'arquitectura', 'filosofia', 'hipopotamo', 'ornitorrinco']

class JuegoAhorcado:
    """Clase que maneja el juego del Ahorcado"""
    
    def __init__(self):
        self.letras_correctas = []
        self.letras_incorrectas = []
        self.intentos = 6
        self.aciertos = 0
        self.juego_terminado = False
        self.palabras_jugadas = []
        self.pistas_usadas = 0
        self.palabra = ""
        self.letras_unicas = 0
        self.estadisticas = {
            'partidas_jugadas': 0,
            'partidas_ganadas': 0,
            'partidas_perdidas': 0,
            'racha_actual': 0,
            'mejor_racha': 0
        }
        self.cargar_estadisticas()
    
    def cargar_estadisticas(self):
        """Carga las estadísticas desde un archivo JSON"""
        if os.path.exists('estadisticas_ahorcado.json'):
            try:
                with open('estadisticas_ahorcado.json', 'r') as archivo:
                    self.estadisticas = json.load(archivo)
            except:
                pass

    def guardar_estadisticas(self):
        """Guarda las estadísticas en un archivo JSON"""
        with open('estadisticas_ahorcado.json', 'w') as archivo:
            json.dump(self.estadisticas, archivo)

    def actualizar_estadisticas(self, gano):
        """Actualiza las estadísticas después de cada partida"""
        self.estadisticas['partidas_jugadas'] += 1
        if gano:
            self.estadisticas['partidas_ganadas'] += 1
            self.estadisticas['racha_actual'] += 1
            if self.estadisticas['racha_actual'] > self.estadisticas['mejor_racha']:
                self.estadisticas['mejor_racha'] = self.estadisticas['racha_actual']
        else:
            self.estadisticas['partidas_perdidas'] += 1
            self.estadisticas['racha_actual'] = 0
        self.guardar_estadisticas()

    def mostrar_estadisticas(self):
        """Muestra las estadísticas del jugador"""
        print('\n' + '=' * 40)
        print('ESTADÍSTICAS')
        print('=' * 40)
        print(f'Partidas jugadas: {self.estadisticas["partidas_jugadas"]}')
        print(f'Partidas ganadas: {self.estadisticas["partidas_ganadas"]}')
        print(f'Partidas perdidas: {self.estadisticas["partidas_perdidas"]}')
        if self.estadisticas['partidas_jugadas'] > 0:
            porcentaje = (self.estadisticas['partidas_ganadas'] / self.estadisticas['partidas_jugadas']) * 100
            print(f'Porcentaje de victorias: {porcentaje:.1f}%')
        print(f'Racha actual: {self.estadisticas["racha_actual"]}')
        print(f'Mejor racha: {self.estadisticas["mejor_racha"]}')
        print('=' * 40 + '\n')

    def elegir_dificultad(self):
        """Permite al jugador elegir la dificultad"""
        while True:
            print('\n--- SELECCIONA LA DIFICULTAD ---')
            print('1. Fácil (4-5 letras)')
            print('2. Medio (6-8 letras)')
            print('3. Difícil (9+ letras)')
            opcion = input('Elige una opción (1-3): ')
            
            if opcion == '1':
                return PALABRAS_FACIL
            elif opcion == '2':
                return PALABRAS_MEDIO
            elif opcion == '3':
                return PALABRAS_DIFICIL
            else:
                print('Opción no válida. Intenta de nuevo.')

    def elegir_palabra(self, lista_palabras):
        """Elige una palabra al azar que no se haya jugado en esta sesión"""
        palabras_disponibles = [p for p in lista_palabras if p not in self.palabras_jugadas]
        
        if not palabras_disponibles:
            print('\n¡Has jugado todas las palabras de esta dificultad!')
            self.palabras_jugadas.clear()
            palabras_disponibles = lista_palabras
        
        palabra_elegida = choice(palabras_disponibles)
        self.palabras_jugadas.append(palabra_elegida)
        letras_unicas = len(set(palabra_elegida))

        return palabra_elegida, letras_unicas

    def pedir_letra(self):
        """Solicita una letra al jugador"""
        letra_elegida = ''
        es_valida = False
        abecedario = 'abcdefghijklmnñopqrstuvwxyz'

        while not es_valida:
            letra_elegida = input("Elige una letra: ").lower()
            
            if letra_elegida in self.letras_correctas or letra_elegida in self.letras_incorrectas:
                print("Ya has usado esa letra. Intenta con otra.")
            elif letra_elegida in abecedario and len(letra_elegida) == 1:
                es_valida = True
            else:
                print("No has elegido una letra correcta")

        return letra_elegida

    def usar_pista(self):
        """Revela una letra aleatoria a cambio de una vida"""
        letras_ocultas = [l for l in set(self.palabra) if l not in self.letras_correctas]
        
        if letras_ocultas:
            letra_revelada = choice(letras_ocultas)
            self.letras_correctas.append(letra_revelada)
            self.pistas_usadas += 1
            print(f'\n¡PISTA! La letra "{letra_revelada}" está en la palabra.')
            return True
        return False

    def mostrar_ahorcado(self, vidas):
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

    def mostrar_nuevo_tablero(self):
        """Muestra el estado actual de la palabra"""
        lista_oculta = []

        for l in self.palabra:
            if l in self.letras_correctas:
                lista_oculta.append(l)
            else:
                lista_oculta.append('-')

        print(' '.join(lista_oculta))

    def calcular_puntuacion(self):
        """Calcula la puntuación basada en varios factores"""
        puntos_base = 100
        puntos_por_vida = self.intentos * 20
        puntos_por_dificultad = len(self.palabra) * 10
        penalizacion_pistas = self.pistas_usadas * 30
        
        puntuacion_total = puntos_base + puntos_por_vida + puntos_por_dificultad - penalizacion_pistas
        return max(puntuacion_total, 0)

    def chequear_letra(self, letra_elegida):
        """Verifica si la letra está en la palabra"""
        fin = False

        if letra_elegida in self.palabra:
            self.letras_correctas.append(letra_elegida)
            self.aciertos += 1
        else:
            self.letras_incorrectas.append(letra_elegida)
            self.intentos -= 1

        if self.intentos == 0:
            fin = self.perder()
        elif self.aciertos == self.letras_unicas:
            fin = self.ganar()

        return fin

    def perder(self):
        """Maneja la lógica cuando el jugador pierde"""
        print("\n" + "=" * 40)
        print("¡GAME OVER!")
        print("=" * 40)
        self.mostrar_ahorcado(0)
        print(f"Te has quedado sin vidas.")
        print(f'La palabra oculta era: "{self.palabra.upper()}"')
        self.actualizar_estadisticas(False)
        return True

    def ganar(self):
        """Maneja la lógica cuando el jugador gana"""
        print("\n" + "=" * 40)
        print("¡FELICITACIONES!")
        print("=" * 40)
        self.mostrar_nuevo_tablero()
        print(f'\n¡Has encontrado la palabra: "{self.palabra.upper()}"!')
        
        puntuacion = self.calcular_puntuacion()
        print(f'Tu puntuación: {puntuacion} puntos')
        print(f'Vidas restantes: {self.intentos}')
        print(f'Pistas usadas: {self.pistas_usadas}')
        
        self.actualizar_estadisticas(True)
        return True

    def mostrar_instrucciones(self):
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

    def menu_principal(self):
        """Muestra el menú principal"""
        while True:
            print('\n' + '=' * 40)
            print('JUEGO DEL AHORCADO')
            print('=' * 40)
            print('1. Jugar')
            print('2. Instrucciones')
            print('3. Ver estadísticas')
            print('4. Salir')
            print('=' * 40)
            
            opcion = input('Elige una opción: ')
            
            if opcion == '1':
                return 'jugar'
            elif opcion == '2':
                self.mostrar_instrucciones()
            elif opcion == '3':
                self.mostrar_estadisticas()
            elif opcion == '4':
                print('\n¡Gracias por jugar! Hasta pronto.')
                return 'salir'
            else:
                print('Opción no válida. Intenta de nuevo.')

    def reiniciar_juego(self):
        """Reinicia las variables para una nueva partida"""
        self.letras_correctas = []
        self.letras_incorrectas = []
        self.intentos = 6
        self.aciertos = 0
        self.juego_terminado = False
        self.pistas_usadas = 0

    def jugar(self):
        """Función principal del juego"""
        self.reiniciar_juego()
        
        lista_palabras = self.elegir_dificultad()
        self.palabra, self.letras_unicas = self.elegir_palabra(lista_palabras)

        while not self.juego_terminado:
            print('\n' + '*' * 40 + '\n')
            self.mostrar_ahorcado(self.intentos)
            self.mostrar_nuevo_tablero()
            print('\n')
            print('Letras incorrectas: ' + ' '.join(self.letras_incorrectas) if self.letras_incorrectas else 'Letras incorrectas: Ninguna')
            print(f'Vidas: {self.intentos}')
            print(f'Pistas usadas: {self.pistas_usadas}')
            print('\n' + '*' * 40 + '\n')
            
            print('¿Qué deseas hacer?')
            print('1. Elegir una letra')
            print('2. Usar una pista (cuesta 1 vida)')
            accion = input('Elige (1 o 2): ')
            
            if accion == '2' and self.intentos > 1:
                if self.usar_pista():
                    self.intentos -= 1
                    self.aciertos = sum(1 for l in set(self.palabra) if l in self.letras_correctas)
                    if self.aciertos == self.letras_unicas:
                        self.juego_terminado = self.ganar()
            elif accion == '1':
                letra = self.pedir_letra()
                self.juego_terminado = self.chequear_letra(letra)
            else:
                print('Opción no válida o no tienes suficientes vidas para una pista.')

    def ejecutar(self):
        """Ejecuta el programa principal"""
        while True:
            accion = self.menu_principal()
            
            if accion == 'salir':
                break
            elif accion == 'jugar':
                self.jugar()
                
                while True:
                    respuesta = input('\n¿Quieres jugar de nuevo? (s/n): ').lower()
                    if respuesta == 's':
                        self.jugar()
                    elif respuesta == 'n':
                        break
                    else:
                        print('Por favor responde "s" para sí o "n" para no.')


# Programa principal
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.ejecutar()