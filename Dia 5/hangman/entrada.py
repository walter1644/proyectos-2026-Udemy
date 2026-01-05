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