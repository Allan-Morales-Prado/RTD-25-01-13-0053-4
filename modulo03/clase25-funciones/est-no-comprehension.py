import math

def media(lista : list[int | float]) -> float:
  return sum(lista) / len(lista)

def sdd(lista : list[int | float], media : int | float):
  # diff = [(elemento - media) ** 2 for elemento in lista]
  suma = 0
  for elemento in lista:
    suma += (elemento - media)**2
  return math.sqrt(suma /(len(lista) - 1))

def resultado(lista : list[int | float]):
  m = media(lista)
  sd = sdd(lista, m)
  # lista_estandarizada = [(valor - m) / sd for valor in lista]
  lista_estandarizada = []
  for valor in lista:
    lista_estandarizada.append((valor - m) / sd)
  return m, sd, lista_estandarizada

lista = [1, 2, 3, 4, 5, 6]

m, desv_st, l_e = resultado(lista)
print("La media es: ", m)
print("La desviación estandard es: ", desv_st)
print("La lista estandarizada es: ", l_e)


