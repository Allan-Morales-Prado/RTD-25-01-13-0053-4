from cap02p2.models import Libro, Autor, AutorLibro

# 1. Crear Autores
a1 = Autor.objects.create(nombre="Donald", apellido="Knuth")
a2 = Autor.objects.create(nombre="Alfred", apellido="Aho")
a3 = Autor.objects.create(nombre="Jeffrey", apellido="Ullman")
a4 = Autor.objects.create(nombre="Terence", apellido="Tao")
a5 = Autor.objects.create(nombre="Gilbert", apellido="Strang")

# 2. Crear Libros sobre Informática y Matemáticas
l1 = Libro.objects.create(titulo="The Art of Computer Programming", year=1968)
l2 = Libro.objects.create(titulo="Compilers: Principles, Techniques, and Tools", year=1986)
l3 = Libro.objects.create(titulo="Introduction to Automata Theory", year=1979)
l4 = Libro.objects.create(titulo="Analysis I", year=2006)
l5 = Libro.objects.create(titulo="Linear Algebra and Its Applications", year=1976)

# -------------------------------------------------------------------
# 3. Asignaciones DESDE AUTOR (autor.libros.add)
# -------------------------------------------------------------------

# Donald Knuth escribe "The Art of Computer Programming"
a1.libros.add(
    l1,
    through_defaults={
        "traduccion": "Original (Inglés)",
        "edicion": 3,
        "creado_por": "admin_tech"
    }
)

# Alfred Aho coescribe "Compilers" (Los Dragones)
a2.libros.add(
    l2,
    through_defaults={
        "traduccion": "Español",
        "edicion": 2,
        "creado_por": "editor_cs"
    }
)

# Terence Tao escribe "Analysis I"
a4.libros.add(
    l4,
    through_defaults={
        "traduccion": "Original (Inglés)",
        "edicion": 4,
        "creado_por": "math_dept"
    }
)

# -------------------------------------------------------------------
# 4. Asignaciones INVERSAS DESDE LIBRO (libro.autores.add)
# -------------------------------------------------------------------

# Asignar a Jeffrey Ullman como coautor del libro "Compilers"
l2.autores.add(
    a3,
    through_defaults={
        "traduccion": "Español",
        "edicion": 2,
        "creado_por": "editor_cs"
    }
)

# Asignar a Jeffrey Ullman y Alfred Aho como coautores de "Introduction to Automata Theory"
l3.autores.add(
    a2, a3,
    through_defaults={
        "traduccion": "Español",
        "edicion": 1,
        "creado_por": "admin_tech"
    }
)

# Asignar a Gilbert Strang al libro "Linear Algebra and Its Applications"
l5.autores.add(
    a5,
    through_defaults={
        "traduccion": "Portugués",
        "edicion": 5,
        "creado_por": "math_dept"
    }
)