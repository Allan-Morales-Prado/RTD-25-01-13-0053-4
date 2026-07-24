from personaje import Personaje
from npc import NPC

class Monstruo(Personaje, NPC):
  
    def __init__(self, **kwargs):
        # ej: kwargs = {"hp" = 1000, "atk" = 1, "df" = 8, "nombre" = "Bégimo"}
        super().__init__(**kwargs)
        # ej: super().__init__(hp = 1000, atk = 1, df = 8, nombre = "Bégimo")
    
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)
      
    def defensa(self, ataque: int) -> int:
        danio_recibido = max(ataque - (self.df + int(self.hp * 0.001)), 0)
        self.hp -= danio_recibido
        return danio_recibido