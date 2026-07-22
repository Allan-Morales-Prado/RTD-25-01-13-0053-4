class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.tomar_prestado(libro)
        return False

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.devolver_libro(libro)
        return False