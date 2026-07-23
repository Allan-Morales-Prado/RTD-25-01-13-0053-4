class Vehiculo:
    def __init__(self, color):
        self.color = color
    
    def describir(self):
        return f"Vehículo de color {self.color}"

class Coche(Vehiculo):
    def __init__(self, color, puertas):
        super().__init__(color)
        self.puertas = puertas
    
    def describir(self):
        return f"Coche con {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, color, cilindrada):
        super().__init__(color)
        self.cilindrada = cilindrada

vehiculos = [
    Coche("Rojo", 4),
    Moto("Azul", 500),
    Vehiculo("Verde")
]

for v in vehiculos:
    print(v.describir())