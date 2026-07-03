def ejemplo(lista):
    resultado = []
    for i in lista:
        resultado.append(i * 2)
    return resultado

numeros = [1, 2, 3, 4]
print(ejemplo(numeros)) # [2, 4, 6, 8]