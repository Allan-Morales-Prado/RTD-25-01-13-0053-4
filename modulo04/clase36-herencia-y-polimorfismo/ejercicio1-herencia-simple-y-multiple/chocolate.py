from sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
  
    def __init__(self, porc_cacao: float):
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)
        
    @abstractmethod
    def validar_porc_cacao(self, porc: float) -> float:
        pass
      
class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc: float) -> float:
        return min(max(0.75, porc), 0.85)
      
class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass
  
if __name__ == '__main__':
    c = ChocolateAmargoSinGluten(0.3)
    print(c.porc_cacao)