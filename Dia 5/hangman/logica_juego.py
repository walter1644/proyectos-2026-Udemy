# ===== ARCHIVO: logica_juego.py =====
# Contiene la lógica principal del juego

from random import choice
from models import EstadoJuego


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
