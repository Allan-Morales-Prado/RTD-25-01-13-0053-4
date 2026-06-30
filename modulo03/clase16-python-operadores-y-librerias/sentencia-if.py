"""
Ejercicio:
Pide la edad del usuario y clasifícala en:

"Niño" (0-12 años)
"Adolescente" (13-17 años)
"Adulto" (18-64 años)
"Jubilado" (65 años o más)
"""

edad = int(input("Ingrese su edad > "))

if edad >= 0 and edad <= 12:
    print("Niño") # edad = 9
elif edad >= 13 and edad <= 17:
    print("Adolescente") # edad = 15
elif edad >= 18 and edad <= 64:
    print("Adulto") # edad = 40
elif edad >= 65: # edad = 88324
    print("Jubilado")
else:
    print("edad no válida")