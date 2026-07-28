def funcion_principal():
    try:
        try:
            datos = {"a": 1, "b": 2}
            valor = datos["c"]
        except KeyError:
            print("Clave no encontrada")
            raise TypeError("Error de tipo")
        finally:
            print("Limpiando recursos internos")
    except TypeError:
        print("Error de tipo capturado externamente")
        raise RuntimeError("Error de ejecución")
    finally:
        print("Limpiando recursos externos")

funcion_principal()