"""
C)

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self) -> float:
        pass
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre
        
D)

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

"""