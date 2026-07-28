from datetime import datetime
from error import HoraError, LargoTextoError
from reunion import Reunion

def validar_hora(hora_str: str) -> datetime.time:
    """Valida hora en formato HH:MM:SS"""
    try:
        return datetime.strptime(hora_str.strip(), "%H:%M:%S").time()
    except ValueError:
        raise HoraError(
            "Formato de hora inválido. Debe ser HH:MM:SS "
            "(ejemplo: 14:30:25)"
        )

def main():
    titulo = None
    hora = None
    
    while True:
        try:
            if titulo is None or len(titulo) > 150:
                titulo = input("\nIngrese título de la reunión (Máximo 150 caracteres):\n")
                if len(titulo) > 150:
                    raise LargoTextoError(
                        "Título de la reunión excede máximo de caracteres",
                        titulo,
                        150
                    )
            
            if hora is None:
                hora_input = input("\nIngrese hora de la reunión (Formato: HH:MM:SS):\n")
                hora = validar_hora(hora_input)
                
        except (HoraError, LargoTextoError) as e:
            print(f"\n{e}\n")
            if isinstance(e, HoraError):
                hora = None
            continue
        else:
            break
    
    r = Reunion(titulo, hora)
    print(f"\n Reunión creada correctamente.")
    print(f"   Título: {r.titulo}")
    print(f"   Hora: {r.hora.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()