class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular_area(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado

figuras = [Circulo(5), Cuadrado(4), Figura("Genérica")]

for f in figuras:
    print(f"{f.nombre}: {f.calcular_area()}")