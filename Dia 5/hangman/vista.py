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