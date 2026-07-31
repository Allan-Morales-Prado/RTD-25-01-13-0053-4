# 📘 Bases de Datos Relacionales

---

# PARTE I: CONCEPTOS FUNDAMENTALES

---

## 🧠 ¿Qué es una Base de Datos?

Una base de datos es una recopilación organizada y estructurada de datos interrelacionados que se almacenan y gestionan electrónicamente en un sistema informático.

```mermaid
flowchart LR
    Cliente["👤 Cliente"] <-->|"SQL"| DBMS["🗄️ DBMS"]
    DBMS <-->|"Lectura/Escritura"| Datos["💾 Datos"]
```

Esta colección de datos está diseñada para facilitar el acceso, la consulta y la administración eficiente de la información relevante en distintos contextos, como empresas u organizaciones.

### Ejemplo práctico: Almacenaje de datos en Twitter

1. Una persona inicia sesión → se almacenan sus datos personales.
2. Un usuario puede crear **1 a muchos tweets**.
3. Los tweets se **relacionan** con el usuario mediante una operación relacional.
4. Los tweets persisten incluso después de cerrar sesión gracias a la base de datos.

---

## 🏢 Rol de las Bases de Datos en la Organización

- Son el **elemento fundamental** que permite a aplicaciones web, móviles y de escritorio contener información de usuarios.
- Permiten obtener datos relevantes mediante **análisis y consultas específicas**.
- Representan la **lógica de negocio** en el **Backend** de una aplicación.

---

## ⚙️ RDBMS (Relational Database Management System)

Un **Sistema de Gestión de Bases de Datos Relacionales** permite:

| Acción | Descripción |
|--------|-------------|
| **Crear** | Elementos en una base de datos |
| **Leer** | La información almacenada |
| **Actualizar** | Los datos existentes |
| **Eliminar** | Registros específicos |

---

## 📊 Estructura de una Base de Datos Relacional

> Similar a un archivo Excel:

- **Tablas**: Contienen los datos.
- **Registros (filas)**: Cada fila representa una entidad.
- **Campos (columnas)**: Atributos de la entidad.
- **Valores**: Datos específicos en cada campo.

---

## 💬 SQL (Structured Query Language)

Lenguaje estándar para:

- Consultar información.
- Manipular datos.
- Definir estructuras de datos.

---

# PARTE II: INSTALACIÓN Y PRÁCTICA

---

## 🛠️ Instalación de PostgreSQL

> **Ventaja:** Tener PostgreSQL instalado localmente nos permite **mayor control** y prepara nuestro entorno de desarrollo.

### 🪟 Instalación en Windows

1. Ir a la página oficial de PostgreSQL y seleccionar **"Download the installer"**.
2. Elegir la arquitectura del sistema operativo (32 o 64 bits) y seleccionar la **versión 14**.
3. Ejecutar el instalador y seguir las instrucciones.
4. Al finalizar, presionar **Finalizar/Terminar**.
5. Ejecutar **pgAdmin** para probar que todo esté instalado correctamente.
6. Iniciar sesión con la contraseña definida para el administrador.
7. Verificar en el menú izquierdo que el servidor esté corriendo correctamente.

#### ✅ Probando acceso en Windows

Desde el terminal, ejecuta:

```bash
psql -U nombreDeUsuario
```

(El usuario y contraseña son los que definiste durante la instalación)

---

### 🐧 Instalación en Linux

- Consulta la [documentación oficial](https://www.postgresql.org/download/linux/) para instalar según tu distribución.
- Se recomienda instalar también **pgAdmin**.

#### ✅ Probando acceso en Linux

Desde el terminal, ejecuta:

```bash
sudo -u postgres psql
```

---

### 🍎 Instalación en Mac

1. Descarga **Postgres.app** desde su sitio web oficial.
2. Arrastra la aplicación a la carpeta de **Aplicaciones**.
3. Abre Postgres.app y presiona el botón **Start**.
4. (Opcional) Agrega PostgreSQL al **PATH**:

```bash
echo 'export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> [!WARNING]
> Si usas Bash, cambia `~/.zshrc` por `~/.bashrc`.

---

## 🔌 Conectando a una Base de Datos

### Ejercicio Guiado: Conectando con PostgreSQL

| Paso | Comando | Descripción |
|------|---------|-------------|
| **Paso 1** | `psql -U usuario` | Acceder al cliente de PostgreSQL vía terminal |
| **Paso 2** | `CREATE DATABASE prueba1;` | Crear una base de datos llamada `prueba1` |
| **Paso 3** | `\l;` | Listar todas las bases de datos creadas |
| **Paso 4** | `\c prueba1;` | Conectarse a la base de datos `prueba1` |

---

## 🗂️ Principales Objetos de una Base de Datos

| Objeto | Descripción |
|--------|-------------|
| **Tablas** | Almacenan la información que deseamos |
| **Filas** | Representan cada registro ingresado en la base de datos |
| **Columnas** | Muestran un conjunto de datos según los campos definidos en la tabla |

---

## 📝 Creando Tablas y Registros

### Ejercicio Guiado: Agregando tabla y registros a `prueba1`

| Paso | Comando | Descripción |
|------|---------|-------------|
| **Paso 5** | `CREATE TABLE clientes (nombre VARCHAR(50), apellido VARCHAR(50));` | Crear tabla `clientes` con campos `nombre` y `apellido` |
| **Paso 6** | `INSERT INTO clientes (nombre, apellido) VALUES ('Juan', 'Pérez');` | Insertar valores en la tabla |
| **Paso 7** | `SELECT * FROM clientes;` | Consultar los datos ingresados |

---

## 📊 Diagramas de Comandos

Durante el curso, utilizaremos diagramas de comandos como guía visual para:

- Crear tablas
- Insertar registros
- Consultar datos

> [!NOTE]
> No es necesario memorizar todos los comandos ahora, pero sí familiarizarse con ellos, ya que los usaremos constantemente.

---

## ✏️ Ejercicio Propuesto

Con base en el ejercicio guiado:

1. Inserta **5 registros** en la base de datos `prueba1`.
2. Comparte los resultados con tus compañeros y docente.

---

## ✅ Ideas Clave

- Las bases de datos son esenciales para que las aplicaciones almacenen y gestionen información de usuarios.
- Permiten obtener datos alineados con la lógica de negocio.
- Un **RDBMS** permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
- Los datos en bases relacionales se organizan en **tablas**.
- PostgreSQL es el motor utilizado en este curso.
- Un motor puede contener múltiples bases de datos, tablas y registros.
- Tener PostgreSQL instalado localmente nos da **mayor control** sobre el entorno de desarrollo.
- Las **tablas** almacenan la información, las **filas** representan cada registro y las **columnas** representan los campos definidos.
---