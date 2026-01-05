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
