class PelotaDeJuguete():
    def __init__(self, color):
        self.__color = color
        
    ## getter
    @property
    def color(self):
        return self.__color
    
    def rebotar(self, altura: float):
        pass

p = PelotaDeJuguete("amarilla")
# AttributeError: 'PelotaDeJuguete' object has no attribute '__color'
print(p._PelotaDeJuguete__color)