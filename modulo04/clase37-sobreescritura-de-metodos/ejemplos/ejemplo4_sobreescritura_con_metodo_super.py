class PelotaDeDeporte():
    def __init__(self, color: str):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_hexagonos: int):
        super().__init__(color)  # Ejecuta constructor de la clase padre
        self.__cantidad_hexagonos = cantidad_hexagonos
    
    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos

# Uso
pdf = PelotaDeFutbol("Blanco y Negro", 15)
print(pdf.color)              # "Blanco y Negro" (heredado)
print(pdf.cantidad_hexagonos) # 15 (propio)