from medicamento import Medicamento

opcion_ingreso = int(input("¿Desea agregar un medicamento?\n  1. Sí\n  2. No\n>> "))
ingresados = []

while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento\n"))
    m = Medicamento(nombre, stock)
    
    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input("\nIgrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto
    
    print(f"\n***** DATOS MEDICAMENTO \"{m.nombre}\" *****")
    if m.descuento:
        print(f"PRECIO BRUTO: ${m.precio_bruto}")
        print(f"STOCK: {m.stock}")
        print(f"DESCUENTO: {int(m.descuento*100)}%")
        print(f"PRECIO FINAL: ${int(m.precio_final)}")
        print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    
    opcion_ingreso = int(input("¿Desea agregar un medicamento?\n  1. Sí\n  2. No\n>> "))
