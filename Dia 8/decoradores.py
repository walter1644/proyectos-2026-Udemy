from functools import wraps
from typing import Callable


def decorador_turno(func: Callable) -> Callable:
    """Decorador que formatea la presentación del número de turno"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print("Su número es:")
        numero = func(*args, **kwargs)
        print(f"  >>> {numero} <<<")
        print("Aguarde y será atendido")
        print("=" * 40 + "\n")
        return numero
    return wrapper
