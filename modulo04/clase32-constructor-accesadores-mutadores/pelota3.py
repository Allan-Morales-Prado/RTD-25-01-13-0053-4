
class Pelota():
    def __init__(self, color: str, tamanio: int, material: str, precio: int = 3200):
        self.__color = color
        self.__tamanio = tamanio
        self.material = material
        self.precio = precio
        self.forma = "redonda"
    
    @property
    def color(self):
        return self.__color
      
    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color
    
    @property
    def tamanio(self):
        return self.__tamanio
        
    @tamanio.setter
    def tamanio(self, nuevo_tamanio):
        self.__tamanio = nuevo_tamanio
        
        
if __name__ == '__main__':
    p = Pelota("Amarillo", 16, "plástico")
    # Salida: Amarillo 16 plástico
    