# A continuación, se muestra cómo crear un programa que filtre todos los números de una lista que sean menores a 1000. Esto es lo mismo que decir "seleccionar todos los elementos mayor o iguales a mil".
# Transformarlo en un List Comprehension


a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = [elemento if elemento >= 1000 else None for elemento in a]
## Marcela: [elemento for elemento in a if (elemento)>= 1000]
## Ignacio: filtered_array = [elemento if elemento >= 1000 else None for elemento in a]

# for i in range(n):
#     if a[i] >= 1000:
#         filtered_array.append(a[i])
        
print(filtered_array)
