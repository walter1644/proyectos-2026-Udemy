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
