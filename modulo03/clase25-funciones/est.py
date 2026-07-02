import math

def media(lista : list[int | float]) -> float:
  return sum(lista) / len(lista)

def sdd(lista : list[int | float], media : int | float):
  diff = [(elemento - media) ** 2 for elemento in lista]
  return math.sqrt(sum(diff) / (len(lista) - 1))

def resultado(lista : list[int | float]):
  m = media(lista)
  sd = sdd(lista, m)
  lista_estandarizada = [(valor - m) / sd for valor in lista]
  return m, sd, lista_estandarizada

# Defino mi función y sus parámetros
def duplicar():
  pass

# Invoco mi función, ingresando sus argumentos
print("valor duplicado: ", duplicar())

lista = [1, 2, 3, 4, 5, 6]

m, desv_st, l_e = resultado(lista)
print("La media es: ", m)
print("La desviación estandard es: ", desv_st)
print("La lista estandarizada es: ", l_e)


