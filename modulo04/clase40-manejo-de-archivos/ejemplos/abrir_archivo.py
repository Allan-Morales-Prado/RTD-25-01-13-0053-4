ruta_archivo = "index.html"

while True:
    opcion = input("""
Ingrese el número de la opción correspondiente:
1. Leer archivo completo
2. Leer línea por línea
3. Iterar sobre líneas
4. Salir
""")
    
    if opcion == "1":
        pagina = open(ruta_archivo, encoding="utf-8")
        contenido = pagina.read() ## <----
        print(contenido)
        pagina.close()
    elif opcion == "2":
        pagina = open(ruta_archivo, encoding="utf-8")
        lineas = pagina.readlines() ## <----
        # print(lineas)
        for nro_linea in range(len(lineas)):
            print(f"{nro_linea + 1}: {lineas[nro_linea].rstrip("\n")}")
        pagina.close()
    elif opcion == "3":
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    elif opcion == "4":
        break
