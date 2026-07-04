def crear_diccionario(**datos):
    print(type(datos))
    return datos

resultado = crear_diccionario(nombre="Ana", ciudad="Madrid", edad=30)
print(resultado)