class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False
    
if __name__ == '__main__':
    ## Prueba de método no estático prestar()
    lb = Libro("Cien años de soledad", "Gabriel García Marquez", "9788420471839")
    print(f"¿Prestado?: {"Sí" if lb.prestado else "No"}")
    lb.prestar()
    print(f"¿Prestado?: {"Sí" if lb.prestado else "No"}")
    lb.devolver()
    print(f"¿Prestado?: {"Sí" if lb.prestado else "No"}")