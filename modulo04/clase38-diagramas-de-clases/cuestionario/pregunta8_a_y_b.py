"""
A)
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        return "Motor encendido"

class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        
B)
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        return "Motor encendido"

class Coche(Motor):
    def __init__(self, marca, modelo, tipo, potencia):
        super().__init__(tipo, potencia)
        self.marca = marca
        self.modelo = modelo
"""
