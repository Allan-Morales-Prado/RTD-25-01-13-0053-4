"""
C)
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        return "Motor encendido"

D)
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        return "Motor encendido"

class Coche:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor, 150)
    
    def arrancar(self):
        return self.motor.encender()
"""
