class Pelota():
    forma = "redonda"
    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
    
    # Método de instancia que lee color de la instancia
    def lee_color(self):
        print("El color de esta pelota es {}".format(self.color))
    
    def lee_color_local_y_atributo(self, color_local: str):
        color = color_local
        if self.color != color:
            print("El color {} NO es el color de ESTA pelota".format(color))
        else:
            print(f"El color {color} COINCIDE con el color de ESTA pelota")
        
if __name__ == "__main__":
    pass