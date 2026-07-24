class Pelota:
    def __init__(self, color: str):
        print(f"-> Inicializando la base Pelota (Color: {color})")
        self.color = color

class PelotaDeDeporte(Pelota):
    def __init__(self, tamanio: int, color: str):
        # Llamada manual a la base
        Pelota.__init__(self, color) 
        print("Creando pelota de deporte")
        self.tamanio = tamanio

class PelotaDePlastico(Pelota):
    def __init__(self, material: str, color: str):
        # Llamada manual a la base
        Pelota.__init__(self, color) 
        print("Creando pelota de plástico")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, tamanio: int, material: str, color: str):
        # Llamadas manuales secuenciales
        PelotaDeDeporte.__init__(self, tamanio, color)
        PelotaDePlastico.__init__(self, material, color)
        print("Creando pelota de ping pong")
        self.timbre = timbre

# Instanciación
pdpp = PelotaDePingPong(timbre="POWERTI", tamanio=4, material="plástico", color="Blanco")
