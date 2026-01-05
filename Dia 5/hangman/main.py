# ===== ARCHIVO: main.py =====
# Punto de entrada del programa


from vista import Vista
from entrada import GestorEntrada
from palabras import GestorPalabras
from persistencia import GestorPersistencia
from models import Estadisticas
from controlador import ControladorJuego



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