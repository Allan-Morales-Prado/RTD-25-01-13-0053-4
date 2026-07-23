class Vehiculo:
    def arrancar(self):
        return "Motor encendido"
    
    def detener(self):
        return "Motor apagado"

class Coche(Vehiculo):
    def arrancar(self):  # Sobreescrito
        return "Motor encendido con llave"
    
    # detener() no se sobreescribe

coche = Coche()
print(coche.arrancar())  # "Motor encendido con llave" (sobrescrito)
print(coche.detener())   # "Motor apagado" (heredado sin cambios)