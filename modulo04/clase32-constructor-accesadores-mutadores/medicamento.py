# archivo medicamento.py
class Medicamento():
    IVA = 0.18
    
    def __init__(self, nombre: str, stock: int = 0):
        self.__nombre = nombre
        self.__stock = stock
        self.__precio_bruto = 0
        self.__precio_final = 0.0
        self.__descuento = 0.0
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def stock(self):
        return self.__stock
      
    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    
    @property
    def precio_bruto(self):
        return self.__precio_bruto
      
    @precio_bruto.setter
    def precio_bruto(self, precio_bruto):
        self.__precio_bruto = precio_bruto
        
    
    @property
    def descuento(self):
        return self.__descuento
      
    @descuento.setter
    def descuento(self, descuento):
        self.__descuento = descuento
    
    @property
    def precio_final(self):
        return self.__precio_final
      
    @precio_final.setter
    def precio_final(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.__precio_bruto = precio_bruto
            self.__precio_final = precio_bruto * (1 + self.IVA)
        
        if self.__precio_final >= 10000 and self.__precio_final < 20000:
            self.__descuento = 0.1
        elif self.__precio_final >= 20000:
            self.__descuento = 0.2
            
        if self.__descuento:
            self.__precio_final *= 1 - self.__descuento
    
    @staticmethod
    def validar_mayor_a_cero(numero: int) -> bool:
        return numero > 0
      
if __name__ == '__main__':
    m = Medicamento("paracetamol")