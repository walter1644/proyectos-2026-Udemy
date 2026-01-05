from random import choice
import json
import os

# Palabras categorizadas por dificultad
palabras_facil = ['gato', 'perro', 'casa', 'mesa', 'libro', 'agua', 'sol', 'luna']
palabras_medio = ['panadero', 'tiburon', 'guitarra', 'ventana', 'computadora', 'elefante']
palabras_dificil = ['dinosaurio', 'helipuerto', 'arquitectura', 'filosofia', 'hipopotamo', 'ornitorrinco']

# Variables globales del juego
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False
palabras_jugadas = []
pistas_usadas = 0

# Variables de estadísticas
estadisticas = {
    'partidas_jugadas': 0,
    'partidas_ganadas': 0,
    'partidas_perdidas': 0,
    'racha_actual': 0,
    'mejor_racha': 0
}

def cargar_estadisticas():
    """Carga las estadísticas desde un archivo JSON"""
    global estadisticas
    if os.path.exists('estadisticas_ahorcado.json'):
        try:
            with open('estadisticas_ahorcado.json', 'r') as archivo:
                estadisticas = json.load(archivo)
        except:
            pass

def guardar_estadisticas():
    """Guarda las estadísticas en un archivo JSON"""
    with open('estadisticas_ahorcado.json', 'w') as archivo:
        json.dump(estadisticas, archivo)

def actualizar_estadisticas(gano):
    """Actualiza las estadísticas después de cada partida"""
    estadisticas['partidas_jugadas'] += 1
    if gano:
        estadisticas['partidas_ganadas'] += 1
        estadisticas['racha_actual'] += 1
        if estadisticas['racha_actual'] > estadisticas['mejor_racha']:
            estadisticas['mejor_racha'] = estadisticas['racha_actual']
    else:
        estadisticas['partidas_perdidas'] += 1
        estadisticas['racha_actual'] = 0
    guardar_estadisticas()

def mostrar_estadisticas():
    """Muestra las estadísticas del jugador"""
    print('\n' + '=' * 40)
    print('ESTADÍSTICAS')
    print('=' * 40)
    print(f'Partidas jugadas: {estadisticas["partidas_jugadas"]}')
    print(f'Partidas ganadas: {estadisticas["partidas_ganadas"]}')
    print(f'Partidas perdidas: {estadisticas["partidas_perdidas"]}')
    if estadisticas['partidas_jugadas'] > 0:
        porcentaje = (estadisticas['partidas_ganadas'] / estadisticas['partidas_jugadas']) * 100
        print(f'Porcentaje de victorias: {porcentaje:.1f}%')
    print(f'Racha actual: {estadisticas["racha_actual"]}')
    print(f'Mejor racha: {estadisticas["mejor_racha"]}')
    print('=' * 40 + '\n')

def elegir_dificultad():
    """Permite al jugador elegir la dificultad"""
    while True:
        print('\n--- SELECCIONA LA DIFICULTAD ---')
        print('1. Fácil (4-5 letras)')
        print('2. Medio (6-8 letras)')
        print('3. Difícil (9+ letras)')
        opcion = input('Elige una opción (1-3): ')
        
        if opcion == '1':
            return palabras_facil
        elif opcion == '2':
            return palabras_medio
        elif opcion == '3':
            return palabras_dificil
        else:
            print('Opción no válida. Intenta de nuevo.')

def elegir_palabra(lista_palabras):
    """Elige una palabra al azar que no se haya jugado en esta sesión"""
    palabras_disponibles = [p for p in lista_palabras if p not in palabras_jugadas]
    
    if not palabras_disponibles:
        print('\n¡Has jugado todas las palabras de esta dificultad!')
        palabras_jugadas.clear()
        palabras_disponibles = lista_palabras
    
    palabra_elegida = choice(palabras_disponibles)
    palabras_jugadas.append(palabra_elegida)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    """Solicita una letra al jugador"""
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        
        if letra_elegida in letras_correctas or letra_elegida in letras_incorrectas:
            print("Ya has usado esa letra. Intenta con otra.")
        elif letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def usar_pista(palabra_elegida):
    """Revela una letra aleatoria a cambio de una vida"""
    global pistas_usadas
    letras_ocultas = [l for l in set(palabra_elegida) if l not in letras_correctas]
    
    if letras_ocultas:
        letra_revelada = choice(letras_ocultas)
        letras_correctas.append(letra_revelada)
        pistas_usadas += 1
        print(f'\n¡PISTA! La letra "{letra_revelada}" está en la palabra.')
        return True
    return False

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

def mostrar_nuevo_tablero(palabra_elegida):
    """Muestra el estado actual de la palabra"""
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def calcular_puntuacion(vidas_restantes, longitud_palabra, pistas):
    """Calcula la puntuación basada en varios factores"""
    puntos_base = 100
    puntos_por_vida = vidas_restantes * 20
    puntos_por_dificultad = longitud_palabra * 10
    penalizacion_pistas = pistas * 30
    
    puntuacion_total = puntos_base + puntos_por_vida + puntos_por_dificultad - penalizacion_pistas
    return max(puntuacion_total, 0)

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    """Verifica si la letra está en la palabra"""
    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder(palabra_oculta)
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta, vidas)

    return vidas, fin, coincidencias

def perder(palabra):
    """Maneja la lógica cuando el jugador pierde"""
    print("\n" + "=" * 40)
    print("¡GAME OVER!")
    print("=" * 40)
    mostrar_ahorcado(0)
    print(f"Te has quedado sin vidas.")
    print(f'La palabra oculta era: "{palabra.upper()}"')
    actualizar_estadisticas(False)
    return True

def ganar(palabra_descubierta, vidas_restantes):
    """Maneja la lógica cuando el jugador gana"""
    print("\n" + "=" * 40)
    print("¡FELICITACIONES!")
    print("=" * 40)
    mostrar_nuevo_tablero(palabra_descubierta)
    print(f'\n¡Has encontrado la palabra: "{palabra_descubierta.upper()}"!')
    
    puntuacion = calcular_puntuacion(vidas_restantes, len(palabra_descubierta), pistas_usadas)
    print(f'Tu puntuación: {puntuacion} puntos')
    print(f'Vidas restantes: {vidas_restantes}')
    print(f'Pistas usadas: {pistas_usadas}')
    
    actualizar_estadisticas(True)
    return True

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

def menu_principal():
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
            mostrar_instrucciones()
        elif opcion == '3':
            mostrar_estadisticas()
        elif opcion == '4':
            print('\n¡Gracias por jugar! Hasta pronto.')
            return 'salir'
        else:
            print('Opción no válida. Intenta de nuevo.')

def reiniciar_juego():
    """Reinicia las variables para una nueva partida"""
    global letras_correctas, letras_incorrectas, intentos, aciertos, juego_terminado, pistas_usadas
    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    aciertos = 0
    juego_terminado = False
    pistas_usadas = 0

def jugar_ahorcado():
    """Función principal del juego"""
    global palabra, letras_unicas, juego_terminado, intentos, aciertos
    
    reiniciar_juego()
    
    lista_palabras = elegir_dificultad()
    palabra, letras_unicas = elegir_palabra(lista_palabras)

    while not juego_terminado:
        print('\n' + '*' * 40 + '\n')
        mostrar_ahorcado(intentos)
        mostrar_nuevo_tablero(palabra)
        print('\n')
        print('Letras incorrectas: ' + ' '.join(letras_incorrectas) if letras_incorrectas else 'Letras incorrectas: Ninguna')
        print(f'Vidas: {intentos}')
        print(f'Pistas usadas: {pistas_usadas}')
        print('\n' + '*' * 40 + '\n')
        
        print('¿Qué deseas hacer?')
        print('1. Elegir una letra')
        print('2. Usar una pista (cuesta 1 vida)')
        accion = input('Elige (1 o 2): ')
        
        if accion == '2' and intentos > 1:
            if usar_pista(palabra):
                intentos -= 1
                aciertos = sum(1 for l in set(palabra) if l in letras_correctas)
                if aciertos == letras_unicas:
                    juego_terminado = ganar(palabra, intentos)
        elif accion == '1':
            letra = pedir_letra()
            intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
            juego_terminado = terminado
        else:
            print('Opción no válida o no tienes suficientes vidas para una pista.')

# Programa principal
cargar_estadisticas()

while True:
    accion = menu_principal()
    
    if accion == 'salir':
        break
    elif accion == 'jugar':
        jugar_ahorcado()
        
        while True:
            respuesta = input('\n¿Quieres jugar de nuevo? (s/n): ').lower()
            if respuesta == 's':
                jugar_ahorcado()
            elif respuesta == 'n':
                break
            else:
                print('Por favor responde "s" para sí o "n" para no.')