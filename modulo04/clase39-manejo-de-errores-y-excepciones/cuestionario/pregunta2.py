"""
C)

class MiError(Exception):
    def __init__(self):
        super().__init__()

raise MiError("Error personalizado")

D)

class MiError(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

raise MiError()
"""
