import random
pool = [n for n in range(1, 42)]

def sacar_numero(posicion):
  elegido = random.choice(pool)
  pool.remove(elegido)
  print(f"El {posicion}° número sorteado es: {elegido}. Quedan {len(pool)} números en sorteo.")

for i in range(1, 7):
  sacar_numero(i)

elegido = random.choice(pool)
pool.remove(elegido)
print(f"El comodín es: {elegido}, quedaron {len(pool)} en la tómbola.")