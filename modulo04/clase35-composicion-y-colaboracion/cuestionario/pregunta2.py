class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def encender(self):
        return f"Motor {self.tipo} encendido"

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)
    
    def arrancar(self):
        return f"{self.marca}: {self.motor.encender()}"

coche = Coche("Toyota", "V8")
print(coche.arrancar())