# Expresión regular del formato de la hora en demo.py

El código en demo.py tiene la siguiente expresión regular compatible con python
```python
time_re = "^(?:(?:([01]?\\d|2[0-3]):)?([0-5]?\\d):)?([0-5]?\\d)$"
```

## **La expresión regular completa:**
```regex
^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$
```

>[!IMPORTANT]
>Las subcadenas `\d` solo son interpretadas por Python si el símbolo `\` forma parte del string. Para lograrlo, es necesario utilizar su secuencia de escape: `\\`.
>
>Recordar: Las secuencias de escape permiten convertir un caracter reservado por el lenguaje de programación a un string, por ejemplo las comillas simples y dobles, el backslash, el símbolo del porcentaje, entre otros.

## Desglose en partes:

### 1. Anclas de inicio y fin
```regex
^ ... $
```
- `^` → Inicio de la cadena
- `$` → Fin de la cadena
- **Propósito**: Asegura que toda la cadena coincida exactamente (sin caracteres extra)

### 2. Los segundos (obligatorio)
```regex
([0-5]?\d)
```
- `[0-5]` → Dígito del 0 al 5 (primer dígito de los segundos)
- `?` → Opcional (puede o no aparecer)
- `\d` → Cualquier dígito (0-9) → **segundo dígito de los segundos**
- **Ejemplos válidos**: `0-9`, `00-59`
- **Ejemplos inválidos**: `60-99` (porque el primer dígito no puede ser 6-9)

### 3. Los minutos (opcional)
```regex
([0-5]?\d):
```
- `([0-5]?\d)` → Misma lógica que los segundos
- `:` → Dos puntos literal
- **Propósito**: Los minutos son opcionales pero si existen, deben ir seguidos de `:`

### 4. Las horas (opcional)
```regex
(?:([01]?\d|2[0-3]):)?
```
- `(?: ... )` → Grupo no capturador (agrupa sin guardar el resultado)
- `([01]?\d|2[0-3])` → **Dos posibles formatos de hora:**
  - `[01]?\d` → 00-19 (dígito 0 o 1 opcional + cualquier dígito)
  - `|` → O (alternativa)
  - `2[0-3]` → 20-23 (dígito 2 + dígito 0-3)
- `:` → Dos puntos literal
- `?` → Todo el grupo es opcional

## Estructura jerárquica:

```regex
^                      # Inicio de cadena
(?:                    # Grupo principal (todo opcional)
   (?:                 # Grupo de horas (opcional)
      ([01]?\d|2[0-3]) # HORA: 00-23
      :                # Separador
   )?                  # Horas opcionales
   ([0-5]?\d)          # MINUTOS: 00-59
   :                   # Separador
)?                     # Todo el grupo opcional
([0-5]?\d)             # SEGUNDOS: 00-59 (obligatorio)
$                      # Fin de cadena
```

## Ejemplos de coincidencias:

### **Válidos:**
| Entrada | ¿Coincide? | Explicación |
|---------|------------|-------------|
| `30` | ✅ Sí | Solo segundos (30) |
| `5` | ✅ Sí | Solo segundos (05) |
| `:30` | ✅ Sí | Minutos 0, segundos 30 (minutos opcionales) |
| `15:30` | ✅ Sí | Minutos 15, segundos 30 |
| `1:15:30` | ✅ Sí | Hora 1, minutos 15, segundos 30 |
| `23:59:59` | ✅ Sí | Hora máxima válida |
| `00:00:00` | ✅ Sí | Hora mínima válida |

### Inválidos:
| Entrada | ¿Coincide? | Razón |
|---------|------------|-------|
| `:5` | ❌ No | Segundos inválidos (debe ser `:05`) |
| `60` | ❌ No | Segundos > 59 |
| `24:00:00` | ❌ No | Hora > 23 |
| `12:60:00` | ❌ No | Minutos > 59 |
| `12:00:60` | ❌ No | Segundos > 59 |

## Visualización de la estructura:

```
HH:MM:SS  →  Formato completo
   MM:SS  →  Formato sin horas
      SS  →  Solo segundos

Donde:
- HH: 00-23
- MM: 00-59
- SS: 00-59
```

## Analogía

Como en un **reloj digital**:
1. Los **segundos** son **obligatorios** (siempre debe haber al menos segundos)
2. Los **minutos** son **opcionales** (es posible ponerlos o no)
3. Las **horas** son **opcionales** (es posible ponerlas o no)

Pero hay una regla importante: **si se ponen las horas, se deben poner minutos** (no tiene sentido tener, por ejemplo `1::30`).
>---
>## Actividad
>
>1. ¿Por qué `:30` es válido pero `30:` no?
>2. ¿Por qué `1:30` es válido pero `1:30:` no?
>3. ¿Qué pasa con el texto `999`?
>---

## **Consejos didácticos:**

1. **Primero los conceptos básicos**: Enseña `^`, `$`, `\d`, `[]`, `?`, `|`, `()`
2. **Construcción gradual**: Empieza con `\d$` (un dígito) y ve agregando complejidad
3. **Ejercicios prácticos**: Usa [regex101.com](https://regex101.com) para visualizar
4. **Errores comunes**: Adviérteles sobre la confusión entre `?` (opcional) y `?` (cuantificador perezoso)