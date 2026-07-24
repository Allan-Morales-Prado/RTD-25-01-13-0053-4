class Pelota:
    def __init__(self, color: str, **kwargs):
        # Base final antes de 'object'. Limpia el parámetro color.
        super().__init__(**kwargs)
        self.color = color

class PelotaDeDeporte(Pelota):
    def __init__(self, tamanio: int, **kwargs):
        # super() delega al siguiente en el MRO (PelotaDePlastico)
        super().__init__(**kwargs)
        # Se ejecuta al regresar en la cadena: modifica el color base
        self.color = self.color + " Fosforescente"
        print(f"[Deporte] Color modificado a: {self.color}")
        self.tamanio = tamanio

class PelotaDePlastico(Pelota):
    def __init__(self, material: str, **kwargs):
        # Al ser el último intermedio, sube directamente a Pelota
        super().__init__(**kwargs)
        # Se ejecuta al regresar de Pelota: añade su acabado
        self.color = self.color + " Brillante"
        print(f"[Plástico] Color modificado a: {self.color}")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        # Inicia el viaje cooperativo por el MRO
        super().__init__(**kwargs)
        print("Creando pelota de ping pong")
        self.timbre = timbre

# Instanciación
pdpp = PelotaDePingPong(timbre="POWERTI", tamanio=4, material="plástico", color="Blanco")

print(f"\n>>> RESULTADO FINAL EN MEMORIA - Color de la pelota: '{pdpp.color}'")
