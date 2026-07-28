class Error(Exception):
    pass
  
class EdadError(Error):
    def __init__(self, mensaje:str, edad:int):
        self.mensaje = mensaje
        self.edad = edad