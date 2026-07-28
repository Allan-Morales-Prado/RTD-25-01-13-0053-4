from datetime import time

class Reunion():
    def __init__(self, titulo: str, hora: time) -> None:
        self.titulo = titulo
        self.hora = hora
    
    def __str__(self) -> str:
        return f"Reunión: {self.titulo} - Hora: {self.hora.strftime('%H:%M:%S')}"