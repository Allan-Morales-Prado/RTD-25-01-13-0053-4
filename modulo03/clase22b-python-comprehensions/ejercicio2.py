"""
Se tiene una lista con la cantidad de minutos usados en redes sociales de distintos usuarios.
[120, 50, 600, 30, 90, 10, 200, 0, 500]

Se debe retornar una lista que clasifique todos los tiempos menores a 90 minutos como 'bien'
y todos los tiempos mayores o iguales a 90 como 'mal'.

El output debería ser algo similar a lo siguiente:
['mal', 'bien', 'mal', 'bien', 'bien', 'bien', 'mal', 'bien', 'mal']
"""

minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
#clasificacion = ['Bien' if min < 90 else 'Mal' for min in minutos]
clasificacion = ['Mal' if min >= 90 else 'Bien' for min in minutos]
print(clasificacion)