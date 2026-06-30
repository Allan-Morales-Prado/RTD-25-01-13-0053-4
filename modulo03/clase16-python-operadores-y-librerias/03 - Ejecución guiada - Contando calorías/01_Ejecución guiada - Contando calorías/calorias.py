import math
print("\a")
# Equivalente JS: let proteina = parseFloat(prompt(...));
proteina = float(input("Ingrese los gr de proteínas: \n"))
carbohidratos = float(input("Ingrese los gr de carbohidratos: \n"))
grasa = float(input("Ingrese los gramos de grasas: \n"))
# TO DO: nueva entrada: grado alcohólico
# Convención (nomenclatura) nombramiento de variables en Python es snake_case
grado_alcoholico = float(input("Ingrese el grado alcohólico (en unidades): \n"))

# calorias = 4 * (proteina + carbohidratos) + 9 * grasa

calorias_p_c = 4 * (proteina + carbohidratos)
calorias_g = 9 * grasa
calorias_g_a = 7 * grado_alcoholico
calorias_totales = calorias_p_c + calorias_g + calorias_g_a
#calorias = 4 * (proteina + carbohidratos) + 9 * grasa + 7 * grado_alcoholico

## Datos de prueba: 30, 45, 28 y 35 ---> 797
print(f'Las calorías totales del producto son: \
      \n\t 1. calorias obtenidas por Proteinas y Carbohidratos: {math.ceil(calorias_p_c)} \
      \n\t 2. calorias obtenidas por Grasas: {math.ceil(calorias_g)} \
      \n\t 3. calorias obtenidas por Grado Alcohólico: {math.ceil(calorias_g_a)} \
      \n\t calorias TOTALES: {math.ceil(calorias_totales)}')