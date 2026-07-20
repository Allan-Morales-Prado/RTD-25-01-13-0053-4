class Medicamento:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __eq__(self, otro):
        return self.nombre.lower() == otro.nombre.lower()

m1 = Medicamento("Paracetamol")
m2 = Medicamento("paracetamol")
m3 = Medicamento("Ibuprofeno")

print(m1 == m2)
print(m1 == m3)