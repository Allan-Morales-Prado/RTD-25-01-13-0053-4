class Medicamento():
  DESCUENTO = 0.05
  IVA = 0.19

  # crear método estático es_precio_valido
  @staticmethod
  def es_precio_valido(precio: int) -> bool:
    """Función que determina si un precio es válido (positivo)"""
    return precio > 0


if __name__ == "__main__":
  ## Prueba: validación de precios de medicamentos
  precio_medicamento = int(input("Ingrese un precio para el medicamento: "))
  
  es_valido = Medicamento.es_precio_valido(precio_medicamento) # True o False
  if es_valido:
    print("El precio ingresado es válido")
  else:
    print("El precio ingresado no es válido")

  ## Prueba: verificar si los atributos estáticos tienen el mismo valor en varias instancias
  medicamento_1, medicamento_2 = Medicamento(), Medicamento()
  if medicamento_1.IVA == medicamento_2.IVA:
    print("El IVA aplicado a ambos medicamentos es el mismo")

  if medicamento_1.DESCUENTO == medicamento_2.DESCUENTO:
    print("El descuento aplicado a ambos medicamentos es el mismo")

