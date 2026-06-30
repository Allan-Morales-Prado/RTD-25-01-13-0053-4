"""
Tenemos un listado de países y la cantidad de usuarios por cada país en la
siguiente tabla:

| País      | Cantidad de usuarios |
| --------- | -------------------- |
| México    | 70                   |
| Chile     | 50                   |
| Argentina | 55                   |

1. Convertir la tabla mostrada en un diccionario.
2. Filtrar los países con menos de 60 usuarios.
"""

pais = ['México', 'Chile', 'Argentina']
n_usuarios = [70, 50, 55]

usuarios_por_pais = {p:u for p, u in zip(pais, n_usuarios) if u < 60}
print(usuarios_por_pais)

# Mostrar solo los nombres de los paises con menos de 60 usuarios
# filtro = [p for p, v in zip(pais, n_usuarios) if v < 60]
# print("Países con menos de 60 usuarios: ", filtro)

# Mostrar paises con menos de 60 usuarios (incluida la cantidad de usuarios)
# filtro_2 = {p:v for p, v in usuarios_por_pais.items() if v < 60}
# print("Países con menos de 60 usuarios: ", filtro_2)