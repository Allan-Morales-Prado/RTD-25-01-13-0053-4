import random
pool = [n for n in range(1, 42)]

def sacar_numero(posicion):
  global pool
  elegido = random.choice(pool)
  pool.remove(elegido)
  print(f"El {posicion}° número sorteado es: {elegido}")

for i in range(1, 7):
  sacar_numero(i)

elegido = random.choice(pool)
pool.remove(elegido)
print(f"El comodín es: {elegido}")