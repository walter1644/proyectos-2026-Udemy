from datetime import datetime


class Turno:
    """Representa un turno individual"""
    
    def __init__(self, numero: str, area: str, prioridad: bool = False):
        self.numero = numero
        self.area = area
        self.timestamp = datetime.now()
        self.atendido = False
        self.prioridad = prioridad #True: True para embarazadas, adultos mayores,etc.

    def marcar_atendido(self):
        """Marca el turno como atendido"""
        self.atendido = True
    
    def to_dict(self) -> dict:
        """Convierte el turno a diccionario para guardar"""
        return {
            'numero': self.numero,
            'area': self.area,
            'timestamp': self.timestamp.isoformat(),
            'atendido': self.atendido
        }
    
    def __str__(self):
        estado = "🟢 Atendido" if self.atendido else "🔴 En espera"
        return f"{self.numero} - {estado}"
