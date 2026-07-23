class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):  # Sobreescritura
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):  # Sobreescritura
        return "¡Miau!"

# Uso
animales = [Animal(), Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())
# Salida:
# Sonido genérico
# ¡Guau!
# ¡Miau!