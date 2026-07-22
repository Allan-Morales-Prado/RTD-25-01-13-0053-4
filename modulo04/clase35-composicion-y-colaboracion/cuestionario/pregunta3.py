"""
C)class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

  class Curso:
    def __init__(self, nombre, estudiante):
        self.nombre = nombre
        self.estudiante = estudiante
        
D)class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

  class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

"""

"""Se necesita implementar un sistema donde un objeto Curso 
  contenga una lista de Estudiantes. Los estudiantes pueden existir 
  independientemente del curso
  y pueden estar inscritos en múltiples cursos simultáneamente. 
  ¿Cuál opción implementa correctamente esta relación?"""