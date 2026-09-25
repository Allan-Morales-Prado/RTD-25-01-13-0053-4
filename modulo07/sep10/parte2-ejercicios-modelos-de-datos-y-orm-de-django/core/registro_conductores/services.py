from .models import Conductor, Direccion, Vehiculo

def crear_conductor(
    rut: str,
    nombre: str,
    apellido: str,
    fecha_nac: str
):
    nuevo_conductor = Conductor.objects.create(
      rut=rut,
      nombre=nombre,
      apellido=apellido,
      fecha_nac=fecha_nac
    )
    print(f"Creado en la base de datos: {nuevo_conductor}")

def agregar_direccion_a_conductor(
  conductor: Conductor,
  calle: str,
  numero: str,
  dpto: str,
  comuna: str,
  ciudad: str,
  region: str
):
    nueva_direccion = Direccion.objects.create(
      calle=calle,
      numero=numero,
      dpto=dpto,
      comuna=comuna,
      ciudad=ciudad,
      region=region,
      conductor=conductor
    )
    print(f"Dirección registrada: {nueva_direccion}, asignado a: {nueva_direccion.conductor}")
    

def agregar_un_vehiculo(
  patente: str,
  marca: str,
  modelo: str,
  year: str,
  conductor: Conductor
):
    nuevo_vehiculo = Vehiculo.objects.create(
      patente=patente,
      marca=marca,
      modelo=modelo,
      year=year,
      conductor=conductor
    )
    print(f"Vehiculo registrado: {nuevo_vehiculo}, asignado a: {nuevo_vehiculo.conductor}")
  
def eliminar_vehiculo(patente: str):
    vehiculo = Vehiculo.objects.get(patente=patente)
    if vehiculo:
        vehiculo.delete()
    else:
        print("Vehiculo no encontrado")
  
def eliminar_conductor(rut: str):
    conductor = Conductor.objects.get(rut=rut)
    if conductor:
      conductor.delete()
    else:
      print("Conductor no encontrado")