import random
from personaje import Personaje

class Jugador(Personaje):
    def __init__(
        self,
        hp: int,
        atk: int,
        df: int,
        arma: str = None
    ) -> None:
        super().__init__(hp, atk, df)
        self.__arma = arma
        
    @property
    def arma(self) -> str:
        return self.__arma
    
    def ataque(self) -> int:
        return (self.atk + random.randint(1,5) if self.arma else self.atk)
    
    def defensa(self, ataque: int) -> int:
        danio_recibido = max(ataque - random.randint(1, self.df), 0)
        self.hp -= danio_recibido
        return danio_recibido