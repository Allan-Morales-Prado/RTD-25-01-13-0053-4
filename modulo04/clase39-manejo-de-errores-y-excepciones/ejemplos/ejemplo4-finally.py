from errores import EdadError
intentos = 1
while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        if edad < 0:
            # raise Exception("Edad debe ser un N° positivo.")
            raise EdadError("Edad debe ser un N° positivo", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
        consultar = False
    except ValueError:
        print("Debe ingresar un número")
    except EdadError as e:
        print(f"Error en la edad ingresada ({e.edad}). {e.mensaje}")
        # Más instrucciones
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        print(f"Intentos ({intentos} de 3)")
        intentos += 1