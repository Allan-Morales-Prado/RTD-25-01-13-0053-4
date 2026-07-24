class Pelota:
    def __init__(self, color: str):
        self.color = color

class PelotaDeDeporte(Pelota):
    def __init__(self, tamanio: int, color: str):
        Pelota.__init__(self, color) 
        # Modificación legítima: Las pelotas de deporte usan colores fosforescentes para visibilidad
        self.color = self.color + " Fosforescente"
        print(f"[Deporte] Color establecido en: {self.color}")
        self.tamanio = tamanio

class PelotaDePlastico(Pelota):
    def __init__(self, material: str, color: str):
        Pelota.__init__(self, color) 
        # Modificación legítima: El plástico al moldearse queda con acabado brillante
        self.color = self.color + " Brillante"
        print(f"[Plástico] Color establecido en: {self.color}")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, tamanio: int, material: str, color: str):
        # LLAMADAS MANUALES SECUENCIALES
        PelotaDeDeporte.__init__(self, tamanio, color)
        PelotaDePlastico.__init__(self, material, color)
        self.timbre = timbre

# Instanciamos una pelota que inicialmente queremos que sea de color "Blanco"
pdpp = PelotaDePingPong(timbre="POWERTI", tamanio=4, material="plástico", color="Blanco")

print(f"\n>>> RESULTADO FINAL EN MEMORIA - Color de la pelota: '{pdpp.color}'")