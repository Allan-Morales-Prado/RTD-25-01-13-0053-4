import sys
from medicamento import Medicamento

# CLI
m1 = Medicamento(nombre = sys.argv[1], stock = int(sys.argv[2]))
m1.precio_final = float(sys.argv[3])

print(f"El precio bruto del medicamento {m1.nombre} es ${int(m1.precio_bruto)}")

if m1.descuento:
    print(f"Tiene un descuento de {int(m1.descuento * 100)}%")
    
print(f"El precio final del medicamento es ${int(m1.precio_final)}")