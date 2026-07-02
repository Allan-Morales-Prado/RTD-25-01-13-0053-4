# listas dentro de otras
listas_anidadas = [
  [0, 3, 4], # 0
  ['apple', 'juice'], # 1
  [[True], [0, 1, 0], [5.12, -32]],
  {'nombre': 'TVBox', 'sistema operativo': 'armbian'}
]

notas_matematicas = {
  'Allan': [6.8, 6.2, 6.0],
  'Alejandra': [7.0, 6.1, 5.9]
}

print(type(notas_matematicas['Allan'][2]))
notas_matematicas['Allan'][2] = 6.5
print(notas_matematicas['Allan'][2])
# print(list(listas_anidadas[3].keys())[1])