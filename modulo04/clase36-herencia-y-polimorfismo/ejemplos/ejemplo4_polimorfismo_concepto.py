class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

# Polimorfismo en acción
figuras = [Circulo(5), Rectangulo(4, 6)]
for figura in figuras:
    print(f"Área: {figura.area()}")