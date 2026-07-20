class Vehiculo:
    def mover(self):
        print("El vehículo se mueve")

class Coche(Vehiculo):
    def mover(self):
        print("El coche acelera")

class Moto(Vehiculo):
    pass

vehiculo = Vehiculo()
coche = Coche()
moto = Moto()

vehiculo.mover()
coche.mover()
moto.mover()