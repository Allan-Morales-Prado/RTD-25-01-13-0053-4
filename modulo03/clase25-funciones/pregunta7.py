def numeros(a, b):
  return a, b, a + b, a * b

numero1, numero2, numero3, numero4 = numeros(2, 3)
mi_tupla = numeros(2, 3)
# numero1, numero2 = (2, 3)
"""
numero1 = 2
numero2 = 3
"""
print(f"numero 1 = {numero1},  numero 2 = {numero2}, numero 3 = {numero3} y numero 4 = {numero4}")
print(mi_tupla)