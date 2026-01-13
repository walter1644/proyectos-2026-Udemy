from functools import wraps  # Importa wraps para preservar metadata de funciones
from typing import Callable  # Importa type hint para funciones


def decorador_turno(func: Callable) -> Callable:  # Define decorador que recibe y retorna función (Callable) que es muy generica (modificar)
    """Decorador que formatea la presentación del número de turno
    wraps preserva la metadata de la función original y wrapper la envuelve."""
    @wraps(func)  # Preserva nombre, docstring y otros atributos de func
    def wrapper(*args, **kwargs):  # Función interna que acepta cualquier argumento
        print("\n" + "=" * 40)  # Imprime salto de línea y línea de 40 signos igual
        print("Su número es:")  # Imprime mensaje informativo
        numero = func(*args, **kwargs)  # Ejecuta función original y guarda resultado
        print(f"  >>> {numero} <<<")  # Imprime número con formato destacado
        print("Aguarde y será atendido")  # Imprime mensaje de espera
        print("=" * 40 + "\n")  # Imprime línea de cierre y salto de línea
        return numero  # Retorna el número generado
    return wrapper  # Retorna función decorada
