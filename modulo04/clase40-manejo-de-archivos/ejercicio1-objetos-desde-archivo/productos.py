import json

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

instancias = []
registros_procesados = 0

with open("productos.txt", encoding="utf-8") as archivo:
    for linea in archivo:
        registros_procesados += 1
        
        if linea == "\n":
            registros_procesados += 1
            continue
        
        try:
            producto = json.loads(linea)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            print(f"Error en registro {registros_procesados}: {e}")
        else:
            nombre_producto = producto.get("nombre")
            precio_producto = producto.get("precio")
            
            if not nombre_producto or precio_producto is None:
                continue
            
            instancias.append(
                Producto(producto.get("nombre"), producto.get("precio"))
            )
            

if __name__ == "__main__":
    for i in range(len(instancias)):
        print(f"{i + 1}. {instancias[i].nombre}: ${instancias[i].precio}")