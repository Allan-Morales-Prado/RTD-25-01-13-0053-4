class Dato:
    def __init__(self, valor : int | float):
        self.valor = valor
    
    def __str__(self) -> str:
        return f"{self.valor}"
    
    def __add__(primer_objeto, segundo_objeto):
        return Dato(primer_objeto.valor + segundo_objeto.valor)
    
    def __sub__(self, instance):
        return Dato(self.valor - instance.valor)

# __getattr__ implícito
dato_a = Dato(10) # __init__ implícito
dato_b = Dato(30) # __init__ implícito

if __name__ == '__main__':
    print(dato_a - dato_b)  # __sub__ --> __str__ implícito