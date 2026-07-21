from abc import ABC, abstractmethod

class Instrumento(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self._estado = "apagado"
    
    @abstractmethod
    def tocar(self):
        pass
    
    def encender(self):
        self._estado = "encendido"
        print(f"{self.nombre} está {self._estado}")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")
    
    def tocar(self):
        print("¡Rasgueo de cuerdas!")

g = Guitarra()
g.encender()
g.tocar()