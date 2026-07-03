def get_multiple(diccionario, *claves):
  #return {clave: diccionario[clave] for clave in claves if clave in diccionario.keys()}
  diccionario_salida = {}

  for password in claves:
    if password in diccionario.keys():
      diccionario_salida[password] = diccionario[password]
  
  return diccionario_salida

diccionario_prueba = {
  'manzana': 'verde',
  'platano': 'amarillo',
  'frutilla': 'roja'
}

print(get_multiple(diccionario_prueba, 'mora', 'platano'))