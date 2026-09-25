from django.db import models
from django.conf import settings
from django.db.models.functions import Now
from django.core.validators import MinValueValidator, MaxValueValidator

class Idioma(models.Model):
    """Catálogo de idiomas según ISO 639."""
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Pais(models.Model):
    """Catálogo de países según ISO 3166-1."""
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    """
    Autor externo al sistema. No es usuario.
    Firma contratos con editoriales para licenciar sus obras.
    """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.ForeignKey(
        Pais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="autores",
    )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        constraints = [
            models.UniqueConstraint(
                fields=["nombre", "apellido"],
                name="unique_autor_nombre_apellido",
            )
        ]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Editorial(models.Model):
    """
    Editorial que publica ediciones.
    Puede ser nacional o extranjera.
    """
    class Tipo(models.TextChoices):
        NACIONAL = "NAC", "Nacional"
        EXTRANJERA = "EXT", "Extranjera"

    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(
        max_length=3,
        choices=Tipo.choices,
        default=Tipo.NACIONAL,
    )
    pais = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        related_name="editoriales",
    )
    sitio_web = models.URLField(blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Libro(models.Model):
    """
    Obra abstracta creada por uno o varios autores.
    Los títulos alternativos se almacenan en TituloLibro.
    """
    year_original = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    sinopsis = models.TextField(blank=True)
    idioma_original = models.ForeignKey(
        Idioma,
        on_delete=models.PROTECT,
        related_name="libros_originales",
    )
    autores = models.ManyToManyField(
        Autor,
        through="LibroAutor",
        related_name="libros",
    )

    class Meta:
        ordering = ["year_original"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        titulo = self.titulo_principal()
        return f"{titulo} ({self.year_original})" if titulo else f"Libro #{self.pk}"

    def titulo_principal(self, idioma=None):
        """
        Devuelve el título principal del libro.
        Si se pasa un idioma, intenta devolver el título en ese idioma;
        si no existe, cae al título original.
        """
        qs = self.titulos.filter(es_principal=True)
        if idioma:
            titulo_idioma = qs.filter(idioma=idioma).first()
            if titulo_idioma:
                return titulo_idioma.titulo
        titulo = qs.first()
        return titulo.titulo if titulo else None


class TituloLibro(models.Model):
    """
    Título alternativo de un libro, por idioma y tipo.
    Permite almacenar el título original y sus traducciones
    (comercial, legal, alternativo) en distintos idiomas.
    """
    class Tipo(models.TextChoices):
        ORIGINAL = "ORI", "Original"
        COMERCIAL = "COM", "Comercial"
        LEGAL = "LEG", "Legal"
        ALTERNATIVO = "ALT", "Alternativo"

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="titulos",
    )
    idioma = models.ForeignKey(
        Idioma,
        on_delete=models.PROTECT,
        related_name="titulos_libro",
    )
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=3,
        choices=Tipo.choices,
        default=Tipo.ORIGINAL,
    )
    es_principal = models.BooleanField(
        default=False,
        help_text="Marca este título como el principal para mostrar en listados.",
    )

    class Meta:
        ordering = ["libro", "idioma", "tipo"]
        verbose_name = "Título de libro"
        verbose_name_plural = "Títulos de libros"
        constraints = [
            models.UniqueConstraint(
                fields=["libro", "idioma", "tipo"],
                name="unique_libro_idioma_tipo",
            )
        ]

    def __str__(self):
        return f"{self.titulo} ({self.idioma.codigo}, {self.get_tipo_display()})"

    def save(self, *args, **kwargs):
        # Si se marca como principal, desmarcar los demás del mismo libro
        if self.es_principal:
            TituloLibro.objects.filter(
                libro=self.libro,
                es_principal=True,
            ).exclude(pk=self.pk).update(es_principal=False)
        super().save(*args, **kwargs)


class LibroAutor(models.Model):
    """
    Relación autor-libro con rol.
    Permite coautoría, traducción, edición y adaptación.
    """
    class Rol(models.TextChoices):
        PRINCIPAL = "PRI", "Autor principal"
        COAUTOR = "COA", "Coautor"
        TRADUCTOR = "TRA", "Traductor"
        EDITOR = "EDI", "Editor"
        ADAPTADOR = "ADA", "Adaptador"

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="libro_autores",
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="autor_libros",
    )
    rol = models.CharField(
        max_length=3,
        choices=Rol.choices,
        default=Rol.PRINCIPAL,
    )
    orden = models.PositiveSmallIntegerField(
        default=1,
        help_text="Orden de aparición en la portada.",
    )

    class Meta:
        ordering = ["libro", "orden"]
        verbose_name = "Autor de libro"
        verbose_name_plural = "Autores de libros"
        constraints = [
            models.UniqueConstraint(
                fields=["libro", "autor", "rol"],
                name="unique_libro_autor_rol",
            )
        ]

    def __str__(self):
        return f"{self.autor} ({self.get_rol_display()}) - {self.libro}"


class Edicion(models.Model):
    """
    Producto comercial concreto: libro + editorial + idioma + territorio.
    Cada edición tiene su propio ISBN y contrato.
    """
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="ediciones",
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        related_name="ediciones",
    )
    idioma = models.ForeignKey(
        Idioma,
        on_delete=models.PROTECT,
        related_name="ediciones",
    )
    territorio = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        related_name="ediciones",
        help_text="Territorio donde se distribuye esta edición.",
    )
    numero = models.PositiveSmallIntegerField(default=1)
    year_publicacion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        null=True,
        blank=True,
        help_text="ISBN-13. Opcional para libros antiguos.",
    )
    adaptacion = models.TextField(
        blank=True,
        help_text="Descripción de la adaptación realizada (cultural, formato, etc.).",
    )
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ediciones_creadas",
    )
    creacion = models.DateTimeField(auto_now_add=True, db_default=Now())

    class Meta:
        ordering = ["libro", "numero"]
        verbose_name = "Edición"
        verbose_name_plural = "Ediciones"
        constraints = [
            models.UniqueConstraint(
                fields=["libro", "editorial", "idioma", "territorio", "numero"],
                name="unique_libro_editorial_idioma_territorio_numero",
            )
        ]

    def titulo_mostrar(self):
        """Devuelve el título en el idioma de esta edición, o el principal."""
        return self.libro.titulo_principal(idioma=self.idioma)

    def __str__(self):
        return (
            f"{self.titulo_mostrar()} "
            f"({self.editorial.nombre}, {self.idioma.codigo}, "
            f"{self.territorio.nombre}, ed. {self.numero})"
        )