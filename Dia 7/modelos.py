"""Módulo de modelos de datos que contiene las clases Persona y Cliente"""

from datetime import datetime
from persistencia import guardar_cliente 


class Persona:
    """Clase base que representa una persona"""
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    """Clase que representa un cliente bancario"""
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)
        self.historial = []

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance:.2f}"

    def depositar(self, monto_deposito):
        """Deposita dinero en la cuenta"""
        if monto_deposito <= 0:
            print("Error: El monto debe ser positivo")
            return False
        self._guardar()

        
        self.balance += monto_deposito
        self._registrar_transaccion("Depósito", monto_deposito)
        print(f"Depósito aceptado. Nuevo balance: ${self.balance:.2f}")
        return True

    def retirar(self, monto_retiro):
        """Retira dinero de la cuenta"""
        if monto_retiro <= 0:
            print("Error: El monto debe ser positivo")
            return False
        self._guardar()
        
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            self._registrar_transaccion("Retiro", monto_retiro)
            print(f"Retiro realizado. Nuevo balance: ${self.balance:.2f}")
            return True
        else:
            print(f"Fondos insuficientes. Balance actual: ${self.balance:.2f}")
            return False

    def _guardar(self):  # ← nuevo método privado (líneas 56-58)
        guardar_cliente(self)

    def _registrar_transaccion(self, tipo, monto):
        """Registra una transacción en el historial"""
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.historial.append({
            'tipo': tipo,
            'monto': monto,
            'fecha': fecha_hora,
            'balance_resultante': self.balance
        })

    def mostrar_historial(self):
        """Muestra el historial de transacciones"""
        if not self.historial:
            print("\nNo hay transacciones registradas")
            return
        
        print("\n" + "="*60)
        print("HISTORIAL DE TRANSACCIONES")
        print("="*60)
        for i, transaccion in enumerate(self.historial, 1):
            print(f"{i}. {transaccion['tipo']} - ${transaccion['monto']:.2f}")
            print(f"   Fecha: {transaccion['fecha']}")
            print(f"   Balance resultante: ${transaccion['balance_resultante']:.2f}")
            print("-"*60)

