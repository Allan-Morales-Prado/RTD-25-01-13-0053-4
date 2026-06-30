"""
Dada la información de ventas de 3 meses:

| Mes       | Ventas |
| --------- | ------ |
| Octubre   | 65000  |
| Noviembre | 68000  |
| Diciembre | 72000  |

1. Convertir la tabla en un diccionario
2. Modificar el diccionario para incrementar las ventas en un 10%.
3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%.
"""

#Ejercicio de ventas

ventas_trimestre = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}
#Aumento del 10%
ventas_actualizadas = {mes: int(ventas * 1.1) for mes, ventas in ventas_trimestre.items()}
print(ventas_actualizadas)
#Disminución del 20% (utilizando como referencia las ventas originales)
ventas_disminuidas = {mes: int(ventas * 0.8) for mes, ventas in ventas_trimestre.items()}
print(ventas_disminuidas)

numeros = [56, -31, 218, 0, 77]
numeros.sort()