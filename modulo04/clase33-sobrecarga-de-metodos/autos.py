class Monoplaza:
    color = ""
    
    def aceleracion(self):
        print("El monoplaza acelera")
        
    def frenado(self):
        print("El monoplaza frena")

class Ferrari(Monoplaza):
    def aceleracion(self):
      print("El monoplaza Ferrari acelera hasta los 300 km/h en 5 segundos")
      
    def frenado(self):
      print("El monoplaza Ferrari frena en 0.5 segundos")
    
ferrari = Ferrari()
ferrari.aceleracion()
ferrari.frenado()

monoplaza = Monoplaza()
monoplaza.aceleracion()