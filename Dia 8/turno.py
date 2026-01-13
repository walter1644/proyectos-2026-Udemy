from datetime import datetime  # Importa clase para trabajar con fechas y horas


class Turno:  # Define clase Turno
    """Representa un turno individual"""
    
    def __init__(self, numero: str, area: str, prioridad: bool = False):  # Constructor con parámetros
        self.numero = numero  # Asigna número de turno al atributo
        self.area = area  # Asigna área al atributo
        self.timestamp = datetime.now()  # Captura fecha y hora actual
        self.atendido = False  # Inicializa estado como no atendido
        self.prioridad = prioridad  # Asigna prioridad (embarazadas, adultos mayores, etc.)

    def marcar_atendido(self):  # Método para cambiar estado del turno
        """Marca el turno como atendido"""
        self.atendido = True  # Cambia atributo a True
    
    def serializar(self) -> dict:  # Método que convierte objeto a diccionario
        """Convierte el turno a diccionario para guardar"""
        return {  # Retorna diccionario con datos del turno
            'numero': self.numero,  # Incluye número de turno
            'area': self.area,  # Incluye área
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M"),  # Formatea fecha y hora
            'atendido': self.atendido, #nueva modificacion
            'prioridad': self.prioridad, #nueva modificacion
            'estado': '🟢 Atendido' if self.atendido else '🔴 En espera',  # Estado con emoji
            'prioridad_texto': "✅ Prioritario" if self.prioridad else "⚪ Normal"  # Prioridad con emoji
        }
    
    @classmethod
    def deserializar(cls, datos: dict) -> 'Turno':
        """Crea un objeto Turno desde un diccionario"""
        turno = cls(
            numero=datos['numero'],
            area=datos['area'],
            prioridad=datos.get('prioridad', False)
        )
        
        # Restaurar timestamp
        turno.timestamp = datetime.strptime(datos['timestamp'], "%Y-%m-%d %H:%M")
        
        # Restaurar estado de atención
        turno.atendido = datos.get('atendido', False)
        
        return turno
    
    def __str__(self):  # Método especial para representación en string
        estado = "🟢 Atendido" if self.atendido else "🔴 En espera"  # Determina emoji según estado
        fecha_hora = self.timestamp.strftime("%Y-%m-%d %H:%M")  # Formatea timestamp
        return f"{self.numero} | {self.area} | {fecha_hora} | {estado}"  # Retorna string formateado
