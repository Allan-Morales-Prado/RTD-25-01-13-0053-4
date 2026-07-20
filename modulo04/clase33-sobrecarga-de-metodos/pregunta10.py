class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Persona: {self.nombre}"
    
    def __repr__(self):
        return f"Persona('{self.nombre}')"

p = Persona("Ana")
print(str(p))
print(repr(p))