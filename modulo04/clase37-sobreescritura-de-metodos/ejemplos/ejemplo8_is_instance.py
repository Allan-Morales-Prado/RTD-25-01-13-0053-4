class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color) -> None:
        self.__color = color

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_hexagonos: int) -> None:
        super().__init__(color)
        self.__cantidad_hexagonos = cantidad_hexagonos
    
    def hacer_pase(self, destino: str, fuerza: int) -> tuple:
        return (destino, fuerza * 0.5)

class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = "Amarillo"
    
    def hacer_saque(self, altura: int, fuerza: int) -> tuple:
        return (altura, altura * fuerza)

# Uso
pdf = PelotaDeFutbol("Blanco y Negro", 15)
pdt = PelotaDeTenis()
pelotas = [pdf, pdf, pdt, pdt, pdf]

for p in pelotas:
    if isinstance(p, PelotaDeTenis) == False:
        p.color = "Roja"
    
    if isinstance(p, PelotaDeFutbol):
        p.hacer_pase("jugador 2", 3)
    elif isinstance(p, PelotaDeTenis):
        p.hacer_saque(2, 3)