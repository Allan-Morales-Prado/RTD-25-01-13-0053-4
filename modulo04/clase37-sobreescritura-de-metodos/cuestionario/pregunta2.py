class Dispositivo:
    def __init__(self, marca):
        self.marca = marca
    
    def encender(self):
        return "Dispositivo encendido"

class Telefono(Dispositivo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def encender(self):
        return f"Teléfono {self.modelo} encendido"

class Tablet(Dispositivo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

dispositivos = [
    Dispositivo("Genérica"),
    Telefono("Samsung", "Galaxy"),
    Tablet("Apple", "iPad")
]

for d in dispositivos:
    print(d.encender())