class Pelota:
    posiciones = [3, 0, 2, 1, 0]
    
    @staticmethod
    def crear_rebote():
        posiciones = [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
        return posiciones
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)
  
if __name__ == "__main__":
  Pelota.imprimir_posiciones()