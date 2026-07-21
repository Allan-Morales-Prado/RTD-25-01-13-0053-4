from abc import ABC, abstractmethod

class Figura(ABC):
  
  @abstractmethod
  def area(self):
    pass
  
  # metodo concreto
  def perimetro(self):
    print("Primetro")