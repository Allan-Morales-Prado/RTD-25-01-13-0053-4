from pelota import Pelota

p = Pelota() # a p se le asigna la CLASE PELOTA, no una instancia de la clase pelota

"""
ERROR: p.asigna_color() no corresponde, es un método de INSTANCIA y p es una CLASE
"""
p.asigna_color(nuevo_color="rojo")
# Salida: El color de esta pelota es rojo
p.lee_color()