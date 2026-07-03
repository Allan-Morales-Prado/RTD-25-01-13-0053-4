from random import choice

pool = []
for n in range(1, 42):
  pool.append(n)

for i in range(1, 7):
  elegido = choice(pool)
  pool.remove(elegido)
  print(f"El {i}° número sorteado es: {elegido}")

elegido = choice(pool)
pool.remove(elegido)
print(f"El comodín es: {elegido}")