continente = "América" # ámbito Global

def mostrar_continente():
  continente = "Asia" # ámbito local
  print(continente)

def mi_funcion():
  continente = "Oceanía"
  mostrar_continente()
  print(continente)

mostrar_continente()
mi_funcion()
print(continente)