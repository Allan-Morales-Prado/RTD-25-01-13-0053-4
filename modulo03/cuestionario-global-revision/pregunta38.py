def multiplicar(factor):
    def interna(numero):
        return numero * factor
    return interna

doble = multiplicar(2)
print(doble(5))