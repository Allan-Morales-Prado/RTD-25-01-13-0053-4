from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

# Uso del sistema
biblioteca = Biblioteca()

# Crear objetos
libro1 = Libro("1984", "George Orwell", "123456789")
libro2 = Libro("Brave New World", "Aldous Huxley", "987654321")
usuario1 = Usuario("Alice", 1)
usuario2 = Usuario("Bob", 2)

# Registrar en la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Operaciones
print(biblioteca.prestar_libro(1, "123456789"))  # True
print(biblioteca.prestar_libro(2, "123456789"))  # False (ya prestado)
print(biblioteca.devolver_libro(1, "123456789")) # True
print(biblioteca.prestar_libro(2, "123456789"))  # True (ahora disponible)