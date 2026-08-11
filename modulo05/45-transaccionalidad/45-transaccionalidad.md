# Transaccionalidad en las operaciones

## ¿Qué es la transaccionalidad?

Las transacciones son **secuencias de instrucciones ordenadas**, las cuales pueden ser indicadas de forma manual o pueden ser aplicadas automáticamente.

### Propiedades de las transacciones (ACID)

La transaccionalidad juega un papel fundamental en la preservación de la integridad de datos. Las propiedades ACID garantizan:

| Propiedad | Descripción |
|-----------|-------------|
| **Atomicidad** | Las operaciones se ejecutan como una unidad completa o no se ejecutan en absoluto. Evita la corrupción de datos. |
| **Consistencia** | Las operaciones llevan la base de datos de un estado consistente a otro. Los datos siempre cumplen con las reglas de negocio y restricciones de integridad. |
| **Aislamiento** | Las operaciones se ejecutan de forma independiente, sin interferirse entre sí. Evita la pérdida de datos. |
| **Durabilidad** | Los cambios realizados se guardan de forma permanente, incluso en caso de fallo del sistema. |

---

## Comandos de transacciones SQL

>[!NOTE]
> Los comandos solo pueden ser usados con las operaciones `INSERT`, `UPDATE` y `DELETE`.

### Sintaxis para iniciar una transacción

```sql
SET TRANSACTION [READ ONLY | WRITE] [NAME nombre_transaccion];
```

- `READ ONLY`: para solamente leer la base de datos.
- `READ WRITE`: para leer y escribir sobre ella, y poder nombrar la transacción con el comando `NAME`.

---

## Flujo de una transacción SQL

Una transacción empaqueta varios pasos en una operación, de forma que se completen todos o ninguno, cuidando la integridad de la información.

```
BEGIN TRANSACTION
    ↓
  Operación 1
    ↓
  Operación 2
    ↓
  Operación 3
    ↓
  ¿Todo correcto?
    ↓           ↓
   SÍ          NO
    ↓           ↓
 COMMIT     ROLLBACK
```

---

## Importancia del modo transaccional

**Caso práctico:** Base de datos de 1000 clientes donde se realiza un giro de dinero y se comete un error en al menos 300 clientes.

- El modo `TRANSACTION` al modificar una base de datos **garantiza la integridad de los datos**.
- Sin el modo transaccional, los datos podrían quedar en un estado inconsistente si se produce un error.
- Con el modo transaccional es posible volver atrás (`ROLLBACK`).

---

## Ejercicio guiado: Commit de transacciones en una cuenta bancaria

### Paso 1: Crear la base de datos y conectarse

```sql
CREATE DATABASE transacciones;
\c transacciones;
```

### Paso 2: Crear la tabla `cuentas`

```sql
CREATE TABLE cuentas (
    numero_cuenta INT NOT NULL UNIQUE PRIMARY KEY,
    balance FLOAT CHECK(balance >= 0.00)
);
```

### Paso 3: Insertar registros

```sql
INSERT INTO cuentas (numero_cuenta, balance) VALUES (1, 1000);
INSERT INTO cuentas (numero_cuenta, balance) VALUES (2, 1000);
```

### Paso 4: Realizar una transferencia

```sql
BEGIN TRANSACTION;
UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 1;
UPDATE cuentas SET balance = balance + 1000 WHERE numero_cuenta = 2;
```

### Paso 5: Verificar el estado de la tabla

```sql
SELECT * FROM cuentas;
```

### Paso 6: Confirmar la transacción

```sql
COMMIT;
```

> Al iniciar con `BEGIN TRANSACTION`, se controlan todas las transacciones. Con `COMMIT` se finaliza la transacción y los cambios se vuelven permanentes.

---

## Rollback (Vuelta atrás)

Permite deshacer las transacciones que se hayan ejecutado, revirtiendo los cambios hasta el último `COMMIT` o `ROLLBACK` ejecutado.

### Ejemplo de Rollback

**Paso 7:** Insertar un nuevo registro

```sql
INSERT INTO cuentas (numero_cuenta, balance) VALUES (3, 1000);
```

**Paso 8:** Iniciar una transacción para transferir

```sql
BEGIN TRANSACTION;
UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 3;
UPDATE cuentas SET balance = balance + 1000 WHERE numero_cuenta = 1;
```

**Paso 9:** Deshacer la transacción

```sql
ROLLBACK;
```

> La base de datos queda con la información del último `COMMIT`.

---

## Save Point (Punto de recuperación)

Permite tener un mayor control de las transacciones, seleccionando qué partes serán descartadas bajo ciertas condiciones, mientras el resto de las operaciones sí se ejecutan.

```sql
SAVEPOINT nombre_punto;
-- operaciones...
ROLLBACK TO nombre_punto;
```

> Todos los cambios realizados entre el punto de recuperación y el `ROLLBACK TO` se descartan.

---

## Modo Autocommit

En PostgreSQL, por defecto viene configurado el modo `AUTOCOMMIT`, lo que significa que implícitamente, una vez realizada una acción sobre la base de datos, ésta realiza un `COMMIT`.

```sql
\echo :AUTOCOMMIT
```

Esto retorna `ON` (activado).

---

## Relación entre integridad de datos y transaccionalidad

| Concepto | Definición |
|----------|------------|
| **Integridad de datos** | Precisión, confiabilidad y consistencia de la información almacenada. |
| **Transaccionalidad** | Conjunto de propiedades que garantizan la ejecución correcta y consistente de las operaciones que modifican los datos. |

### Ejemplos

- **Transferencia bancaria:** La transaccionalidad asegura que la cantidad total de dinero en el sistema se mantenga constante.
- **Reserva de vuelo:** La transaccionalidad asegura que no se asignen dos asientos al mismo pasajero en el mismo asiento.

---

## Buenas prácticas

- Utilizar claves `PRIMARY KEY` y `FOREIGN KEY` para garantizar la integridad referencial.
- Definir reglas de negocio y restricciones de integridad en la base de datos.
- Realizar pruebas exhaustivas de las operaciones que modifican datos.
- Implementar un plan de recuperación ante desastres para proteger la base de datos contra fallos del sistema.

---

## Ideas clave

| Comando | Función |
|---------|---------|
| `BEGIN` | Inicia la transacción; permite ejecutar todas las sentencias SQL necesarias. |
| `COMMIT` | Guarda los cambios de la transacción de forma permanente. |
| `ROLLBACK` | Retrocede los cambios realizados. |
| `SAVEPOINT` | Guarda un punto al cual volver al aplicar `ROLLBACK`. |
| `SET TRANSACTION` | Asigna nombre a la transacción y define su modo. |

### Preguntas de repaso

1. ¿Qué nos permite hacer `COMMIT`?
2. ¿Qué habilita `BEGIN`?
3. ¿Cómo volvemos atrás una transacción SQL?
4. ¿Cuál es el modo por defecto de PostgreSQL con los cambios que se realizan en una base de datos?