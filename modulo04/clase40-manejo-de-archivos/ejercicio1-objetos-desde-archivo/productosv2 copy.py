class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
        
import json
instancias = []

with open("productos.txt", encoding = "utf-8") as productos:
    for linea in productos:
        if not linea:
            continue
        try:
            producto = json.loads(linea)
        except json.JSONDecodeError as e:
            print(f"Error en línea: {linea.strip()} - {e}")
            continue
        else:
            nombre = producto.get("nombre")
            precio = producto.get("precio")
            if not nombre or precio is None:
                instancias.append(
                    Producto(producto.get("nombre"), producto.get("precio"))
                )
                instancias.append(Producto(nombre, precio))