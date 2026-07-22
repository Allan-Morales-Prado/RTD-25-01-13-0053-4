class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro.devolver():
            self.libros_prestados.remove(libro)
            return True
        return False

if __name__ == '__main__':
    from libro import Libro
    
    lb = Libro("Cien años de soledad", "Gabriel García Marquez", "9788420471839")
    usr = Usuario("Allan Morales", "0001")
    
    print(f"¿Prestado?: {"Sí" if lb.prestado else "No"}")
    usr.tomar_prestado(lb)
    
    print(f"¿Prestado?: {"Sí" if lb.prestado else "No"}")
    print(usr.libros_prestados[0].titulo)