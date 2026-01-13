

# ============================================================================
# ARCHIVO: main.py
# ============================================================================

from principal import FarmaciaApp  # Importa clase principal
from os import system  # Importa función system del módulo os

if __name__ == "__main__":  # Si este archivo se ejecuta directamente
    system("cls")  # Limpia la consola (Windows)
    app = FarmaciaApp()  # Crea instancia de la aplicación
    app.ejecutar()  # Ejecuta aplicación