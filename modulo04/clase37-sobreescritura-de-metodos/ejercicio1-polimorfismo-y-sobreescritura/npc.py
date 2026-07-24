class NPC():
    def __init__(self, nombre: str, **kwargs) -> None:
        # nombre = "Bégimo"
        # kwargs = {}
        super().__init__(**kwargs)
        # super().__init__()
        self.__nombre = nombre
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def mostrar_dialogo(self, mensaje: str) -> None:
        print(f"{self.__nombre}: {mensaje}")