from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(
        self,
        hp: int,
        atk: int,
        df: int,
        **kwargs
    ) -> None:
        # kwargs = {"nombre": "Bégimo"}
        super().__init__(**kwargs)
        # super().__init__(nombre = "Bégimo")
        self.__hp = hp
        self.__atk = atk
        self.__df = df
    
    @property
    def hp(self) -> int:
        return self.__hp
    
    @hp.setter
    def hp(self, hp) -> None:
        self.__hp = hp
        
    @property
    def atk(self) -> int:
        return self.__atk
        
    @atk.setter
    def atk(self, atk) -> None:
        self.__atk = atk
            
    @property
    def df(self) -> int:
        return self.__df
        
    @df.setter
    def df(self, df) -> None:
        self.__df = df
    
    @abstractmethod
    def ataque(self) -> int:
        pass
      
    @abstractmethod
    def defensa(self, ataque: int) -> int:
        pass
      
