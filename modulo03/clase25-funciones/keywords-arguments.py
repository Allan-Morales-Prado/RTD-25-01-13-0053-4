def mi_funcion(**datos_personales):
  print("Datos Personales:")
  for k, v in datos_personales.items():
    print(f"{k}: {v}")

mi_funcion(nombre = "Allan", apellido = "Morales", signo = "Cancer", nacionalidad = "Chilena")