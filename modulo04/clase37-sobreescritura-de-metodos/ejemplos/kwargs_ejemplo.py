def mi_funcion(**kwargs):
    for k, v in kwargs.items():
        print(k + ": " + v)

diccionario = {"nombre": "Allan", "apellido":"Morales"}

# mi_funcion(nombre = "Allan", apellido = "Morales")
mi_funcion(**diccionario) ## (nombre = "Allan", apellido = "Morales")