from personaje import Personaje

class Monstruo(Personaje):
  
    def __init__(self, hp, atk, df, arma = "", nombre = ""):
        super().__init__(hp, atk, df, arma)
        self.nombre = nombre
    
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)
      
    def defensa(self, ataque: int) -> int:
        danio_recibido = max(ataque - (self.df + int(self.hp * 0.001)), 0)
        self.hp -= danio_recibido
        return danio_recibido