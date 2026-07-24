from jugador import Jugador
from monstruo import Monstruo

m = Monstruo(hp = 1000, atk = 1, df = 8, nombre = "Bégimo")
m.mostrar_dialogo("GRAAAWR")

enfrentados = [
    Jugador(500, 37, 5, "Ala de Cuervo"),
    m
]

atk = 0

print(f"{enfrentados[0].__class__.__name__} y {enfrentados[1].nombre} ({enfrentados[1].__class__.__name__}) se están enfrentando")

## TO DO:
# Mostrar: acción ejecutada, ej: Jugador ha causado x de daño a Monstruo
# A Monstruo le queda(n) Z puntos de Vida

while not any(e.hp <= 0 for e in enfrentados):
    for e in enfrentados:
        if atk:
            print(f"{e.nombre if e.__class__.__name__ == 'Monstruo' else e.__class__.__name__} ha recibido {e.defensa(atk)} de daño y le queda(n) {e.hp} puntos de salud")
        if e.hp > 0:
            print(f"{e.nombre if e.__class__.__name__ == 'Monstruo' else e.__class__.__name__} ha lanzado un ataque!")
            atk = e.ataque()
        else:
            if isinstance(e, Monstruo):
                print("¡Felicidades!, ¡Haz ganado la batalla!")
            elif isinstance(e, Jugador):
                print("¡Oh no!, haz perdido la batalla :(")