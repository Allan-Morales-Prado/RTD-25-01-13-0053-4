with open("error.log", encoding="utf-8") as archivo:
    archivo.seek(10)
    print(archivo.read(10))
    print(archivo.tell())