class Material:
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota:
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color
        self.material = material  # Material se crea fuera y se pasa como argumento

# El material existe independientemente
m = Material("Plástico", "Corta", "Lisa")
p = Pelota(16, "Amarillo", m)