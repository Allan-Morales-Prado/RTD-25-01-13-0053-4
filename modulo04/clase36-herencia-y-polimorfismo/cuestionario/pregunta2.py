class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    pass

animales = [Perro("Rex"), Gato("Misi"), Animal("Ser")]

for animal in animales:
    print(animal.sonido())