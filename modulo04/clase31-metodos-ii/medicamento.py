class Medicamento():
  DESCUENTO = 0.05
  IVA = 0.19

  # crear método estático es_precio_valido
  @staticmethod
  def es_precio_valido(precio: int) -> bool:
    """Función que determina si un precio es válido (positivo)"""
    return precio > 0
  
  def ingresar_precio(self, precio : int) -> None:
    if Medicamento.es_precio_valido(precio):
      if self.precio >= 10000 and self.precio <= 19999:
        self.descuento = 0.1
      elif self.precio >= 20000 and self.precio <= 29999:
        self.descuento = 0.2
      elif self.precio >= 30000:
        self.descuento = 0.3
      else:
        self.descuento = 0.0
      self.precio = precio * (1 - self.descuento)
    else:
      print("Precio no válido")



if __name__ == "__main__":
  pass