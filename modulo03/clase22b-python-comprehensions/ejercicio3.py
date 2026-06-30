"""
Se tiene una lista con la cantidad de segundos que demoraron algunos procesos.

Se necesita una función para transformar todos los datos a minutos,
(se requiere sólo la parte entera, la parte decimal se puede ignorar).

seconds = [100, 50, 1000, 5000, 1000, 500]

"""
seconds = [100, 50, 1000, 5000, 1000, 500]
minutos = [tiempo // 60 for tiempo in seconds]
print (minutos)