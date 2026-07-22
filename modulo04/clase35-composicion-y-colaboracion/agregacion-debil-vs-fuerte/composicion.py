class Material:
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota:
    def __init__(self, tamanio: int, color: str, textura: str):
        self.tamanio = tamanio
        self.color = color
        # El material se crea dentro del constructor de Pelota
        self.material = Material("Plástico", "Corta", textura)

# El material no existe fuera de la pelota
p = Pelota(16, "Amarillo", "Lisa")