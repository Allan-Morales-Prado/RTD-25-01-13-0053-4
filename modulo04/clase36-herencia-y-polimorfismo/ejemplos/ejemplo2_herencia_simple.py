class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return "Motor encendido"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def abrir_maletero(self):
        return "Maletero abierto"

# Uso
coche = Coche("Toyota", "Corolla", 4)
print(coche.arrancar())      # Heredado de Vehiculo
print(coche.abrir_maletero()) # Método propio de Coche