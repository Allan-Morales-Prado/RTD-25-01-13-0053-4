class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Uso
perro = Perro("Firulais")
gato = Gato("Misi")

print(perro.hacer_sonido())  # ¡Guau!
print(gato.hacer_sonido())   # ¡Miau!