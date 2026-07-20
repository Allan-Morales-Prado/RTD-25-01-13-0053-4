class Pelota():
    def __init__(self):
        self.color = "blanco"
        self.tamanio = 20
        self.material = "plástico"
        
if __name__ == '__main__':
    p = Pelota()
    # Salida: blanco 20 plástico
    print(p.color, p.tamanio, p.material)