class PelotaDeDeporte():
    def __init__(self, tamanio: int, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de deporte")
        self.tamanio = tamanio

class PelotaDePlastico():
    def __init__(self, material: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de plástico")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de ping pong")
        self.timbre = timbre

# El orden de salida cambia debido a la cadena de super()
# Salida:
# Creando pelota de plástico
# Creando pelota de deporte
# Creando pelota de ping pong
pdpp = PelotaDePingPong(tamanio=4, material="plástico", timbre="POWERTI")