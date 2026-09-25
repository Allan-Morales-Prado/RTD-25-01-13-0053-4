from .models import Artista, Grupo, Album, ArtistaGrupo

def crear_artista(nombre:str, apellido:str, instrumento:str, cantante:bool = False):
    return Artista.objects.create(
      nombre=nombre,
      apellido=apellido,
      cantante=cantante,
      instrumento=instrumento
    )

def crear_grupo(nombre:str, fecha_creacion:str):
    return Grupo.objects.create(
      nombre=nombre,
      fecha_creacion=fecha_creacion
    )

def relacion_artista_grupo(artista:Artista, grupo:Grupo, fecha_ingreso:str):
    return ArtistaGrupo.objects.create(
      artista=artista,
      grupo=grupo,
      fecha_ingreso=fecha_ingreso
    )

def agregar_album(titulo:str, year:int, grupo:Grupo):
    return Album.objects.create(
      titulo=titulo,
      year=year,
      grupo=grupo
    )

def obtiene_artista(nombre:str, apellido:str):
    return (
        Artista.objects
        .filter(nombre=nombre)
        .filter(apellido=apellido).first()
    )

def obtiene_grupo(nombre:str):
    return Artista.objects.filter(nombre=nombre).first()

def artista_pertenece_a_grupos(artista:Artista):
    # Buscar artista en ArtistaGrupos
    # Por cada registro encontrado, devolver Grupos
    artista_grupos = ArtistaGrupo.objects.filter(artista__nombre=artista.nombre).filter(artista__apellido=artista.apellido)
    grupos = [ag.grupo for ag in artista_grupos]
    return grupos
      
def grupo_albumes(grupo:Grupo):
    return Album.objects.filter(grupo=grupo)
  
def artista_participa_albumes(artista:Artista):
    grupos = artista_pertenece_a_grupos(artista)
    return [grupo_albumes(g) for g in grupos]
    

