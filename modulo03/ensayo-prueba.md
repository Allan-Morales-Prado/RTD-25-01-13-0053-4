# Ensayo Prueba - Desarrollo de un Sistema de Gestión de Inventario y Ventas en Python

En esta prueba validaremos nuestra capacidad para construir un programa en Python que resuelva un problema del mundo real, utilizando estructuras de datos, funciones, control de flujo y buenas prácticas de programación. Para lograrlo, necesitarás crear varios scripts que interactúen entre sí.

Lee todo el documento antes de comenzar el desarrollo **individual**, para asegurarte de tener el máximo de puntaje y enfocar bien los esfuerzos.

## Descripción del Proyecto

Has sido contratado como desarrollador trainee en **FloraWare Digital** para crear un Sistema de Gestión de Inventario y Ventas. Este sistema permitirá a un pequeño comerciante administrar su stock de productos y registrar ventas.

El sistema debe permitir las siguientes funcionalidades:

1.  **Gestionar un inventario de productos**. Cada producto tendrá:
    - Un **nombre** (string)
    - Un **precio** (float)
    - Una **cantidad en stock** (int)
    - Una **categoría** (string, por ejemplo: "Electrónica", "Ropa", "Alimentos")
    - Un **ID único** (int)

2.  **Registrar ventas**. Una venta consiste en:
    - El **nombre del producto** vendido.
    - La **cantidad** vendida.
    - Calcular el **total de la venta**.
    - Descontar la cantidad vendida del inventario.

3.  **Consultar el inventario**:
    - Ver todos los productos.
    - Buscar un producto por nombre.
    - Filtrar productos por categoría.
    - Identificar productos con stock bajo (menos de 5 unidades).

4.  **Generar un reporte de ventas**:
    - Mostrar el producto más vendido (en cantidad).
    - Mostrar el producto que generó más ingresos (precio unitario * cantidad).
    - Calcular el total de ingresos generados por todas las ventas.

El equipo de desarrollo ha generado un backlog con tareas específicas, las cuales tendrás que desarrollar paso a paso. Cada subtarea consistirá en la creación de un script en Python, que deberá ser testeado dentro del mismo archivo.

Se utilizará la siguiente estructura estándar para cada script:

```python
# Definición de Funciones de la funcionalidad

def func():
    pass

if __name__ == '__main__':
    # Test entregado en cada requerimiento (dado por el Tech Lead)
    pass
```

El archivo `inventario.py` definirá un **diccionario** llamado `productos` que almacenará el inventario inicial. El formato será:

```python
productos = {
    1: {"nombre": "Laptop", "precio": 750000, "stock": 10, "categoria": "Electrónica"},
    2: {"nombre": "Camiseta", "precio": 15000, "stock": 30, "categoria": "Ropa"},
    # ... más productos
}
```

El archivo `ventas.py` definirá una **lista** llamada `historial_ventas` donde se almacenarán todas las ventas realizadas. Cada venta será un diccionario con los campos:

```python
# Ejemplo de una venta en la lista
{
    "nombre": "Laptop",
    "cantidad": 2,
    "total": 1500000,
    "id_producto": 1
}
```

*Se recomienda crear un inventario inicial con al menos 6 productos de diferentes categorías.*

## Requerimientos

### 1. Módulo de Validación (`validador.py`)

Crea un programa llamado `validador.py`. Este módulo se encargará de validar las entradas del usuario.

- Crea la función `validar_opcion()`, la cual debe aceptar como argumentos:
    - `mensaje`: El texto que se mostrará al usuario (ej: "Ingrese su opción: ").
    - `opciones_validas`: Una **lista** de valores permitidos (ej: `["1", "2", "3"]`).
    - `tipo_dato`: El tipo de dato al que se debe convertir la entrada (por defecto `str`).

- La función debe mostrar el `mensaje` y solicitar un valor.
    - Validará que el valor ingresado sea **numérico** si `tipo_dato` es `int` o `float`.
    - Verificará que el valor ingresado esté dentro de `opciones_validas`.
- En caso de error, debe mostrar "Dato inválido. Intente nuevamente." y volver a solicitar el valor.

- La función debe retornar la opción validada y convertida al tipo especificado.

**Tip:** Puedes usar los métodos `isdigit()` para validar números y la función `isinstance()` para validar tipos.

**Test para `validador.py`:**
```python
if __name__ == '__main__':
    print("=== Test Validador ===")
    # Simula la selección de un menú principal (opciones "1","2","3","4","5")
    opcion = validar_opcion("Seleccione una opción (1-5): ", ["1","2","3","4","5"], int)
    print(f"Opción válida: {opcion}")
    
    # Simula la selección de un producto (IDs 1,2,3,4,5,6)
    id_producto = validar_opcion("Ingrese el ID del producto (1-6): ", ["1","2","3","4","5","6"], int)
    print(f"ID de producto válido: {id_producto}")
```

### 2. Módulo de Gestión de Inventario (`gestion_inventario.py`)

Crea un programa llamado `gestion_inventario.py` que contendrá las funciones para manejar el inventario.

- **Función `mostrar_inventario()`**: Toma como argumento el diccionario `productos`. Muestra en pantalla una tabla con todos los productos (ID, Nombre, Precio, Stock, Categoría). Esta función no retorna nada.

- **Función `buscar_producto_por_nombre()`**: Toma como argumentos el diccionario `productos` y el `nombre` a buscar. Retorna el **ID del producto** si se encuentra, o `None` si no existe.

- **Función `filtrar_por_categoria()`**: Toma como argumentos el diccionario `productos` y una `categoria`. Retorna un **nuevo diccionario** con los productos que pertenecen a esa categoría.

- **Función `stock_bajo()`**: Toma como argumento el diccionario `productos` y un `umbral` (por defecto 5). Retorna una **lista** con los nombres de los productos cuyo stock es menor al umbral.

**Test para `gestion_inventario.py`:**
```python
if __name__ == '__main__':
    # Diccionario de prueba
    test_productos = {
        1: {"nombre": "Laptop", "precio": 750000, "stock": 10, "categoria": "Electrónica"},
        2: {"nombre": "Camiseta", "precio": 15000, "stock": 30, "categoria": "Ropa"},
        3: {"nombre": "Manzanas", "precio": 1000, "stock": 3, "categoria": "Alimentos"},
        4: {"nombre": "Auriculares", "precio": 25000, "stock": 2, "categoria": "Electrónica"},
    }
    
    print("=== Prueba de mostrar_inventario ===")
    mostrar_inventario(test_productos)
    
    print("\n=== Prueba de buscar_producto_por_nombre ===")
    id_encontrado = buscar_producto_por_nombre(test_productos, "Auriculares")
    print(f"ID del producto encontrado: {id_encontrado}")
    
    id_no_encontrado = buscar_producto_por_nombre(test_productos, "Televisor")
    print(f"Resultado para producto no encontrado: {id_no_encontrado}")
    
    print("\n=== Prueba de filtrar_por_categoria ===")
    electronicos = filtrar_por_categoria(test_productos, "Electrónica")
    print(f"Productos electrónicos: {electronicos}")
    
    print("\n=== Prueba de stock_bajo ===")
    productos_bajos = stock_bajo(test_productos, 5)
    print(f"Productos con stock bajo: {productos_bajos}")
```

### 3. Módulo de Procesamiento de Ventas (`procesamiento_ventas.py`)

Crea un programa llamado `procesamiento_ventas.py` que permita procesar las ventas.

- **Función `registrar_venta()`**: Toma como argumentos el diccionario `productos`, la lista `historial_ventas`, el `id_producto` y la `cantidad`.
    - Debe verificar que el `id_producto` exista en `productos`.
    - Debe verificar que haya `stock` suficiente para la venta.
    - Si es válido, debe:
        1. Calcular el total de la venta (precio * cantidad).
        2. Crear un diccionario con los datos de la venta y agregarlo a `historial_ventas`.
        3. Descontar la cantidad del stock del producto.
        4. Retornar `True` indicando que la venta fue exitosa.
    - Si no es válido, debe retornar `False` y mostrar el motivo del error.

- **Función `producto_mas_vendido()`**: Toma como argumento la lista `historial_ventas`. Calcula y retorna el **nombre del producto** que más unidades ha vendido.

- **Función `producto_mayor_ingreso()`**: Toma como argumento la lista `historial_ventas`. Calcula y retorna el **nombre del producto** que ha generado más ingresos (suma de los totales de cada venta de ese producto).

- **Función `total_ingresos()`**: Toma como argumento la lista `historial_ventas`. Retorna la suma total de todos los ingresos generados.

**Test para `procesamiento_ventas.py`:**
```python
if __name__ == '__main__':
    # Diccionario de prueba y lista de ventas
    test_productos = {
        1: {"nombre": "Laptop", "precio": 750000, "stock": 10, "categoria": "Electrónica"},
        2: {"nombre": "Camiseta", "precio": 15000, "stock": 30, "categoria": "Ropa"},
        3: {"nombre": "Manzanas", "precio": 1000, "stock": 3, "categoria": "Alimentos"},
    }
    test_ventas = [
        {"nombre": "Laptop", "cantidad": 2, "total": 1500000, "id_producto": 1},
        {"nombre": "Camiseta", "cantidad": 5, "total": 75000, "id_producto": 2},
        {"nombre": "Laptop", "cantidad": 1, "total": 750000, "id_producto": 1},
    ]
    
    print("=== Prueba de registrar_venta ===")
    venta_valida = registrar_venta(test_productos, test_ventas, 1, 1)
    print(f"Resultado de venta válida: {venta_valida}")
    print(f"Historial de ventas actualizado: {test_ventas}")
    print(f"Stock actualizado de Laptop: {test_productos[1]['stock']}")
    
    venta_invalida = registrar_venta(test_productos, test_ventas, 3, 5)
    print(f"Resultado de venta inválida: {venta_invalida}")
    
    print("\n=== Prueba de producto_mas_vendido ===")
    print(f"Producto más vendido: {producto_mas_vendido(test_ventas)}")
    
    print("\n=== Prueba de producto_mayor_ingreso ===")
    print(f"Producto con mayor ingreso: {producto_mayor_ingreso(test_ventas)}")
    
    print("\n=== Prueba de total_ingresos ===")
    print(f"Total de ingresos: {total_ingresos(test_ventas)}")
```

### 4. Módulo de Visualización y Reportes (`reportes.py`)

Crea un programa llamado `reportes.py` que se encargue de mostrar reportes formateados.

- **Función `mostrar_resumen_inventario()`**: Toma como argumento el diccionario `productos`. Debe mostrar:
    - El número total de productos.
    - La cantidad total de unidades en stock.
    - El valor total del inventario (suma de precio * stock para cada producto).

- **Función `mostrar_reporte_ventas()`**: Toma como argumento la lista `historial_ventas`. Debe mostrar en pantalla un reporte formateado:
    - Producto más vendido (en cantidad).
    - Producto con mayores ingresos.
    - Total de ingresos.
    - Número total de ventas realizadas.

- **Función `generar_alerta_stock_bajo()`**: Toma como argumento el diccionario `productos`. Imprime en pantalla una alerta con los productos cuyo stock es menor o igual a 3. Si no hay productos en esa situación, imprime "Todo el stock está en niveles saludables."

**Test para `reportes.py`:**
```python
if __name__ == '__main__':
    test_productos = {
        1: {"nombre": "Laptop", "precio": 750000, "stock": 10, "categoria": "Electrónica"},
        2: {"nombre": "Camiseta", "precio": 15000, "stock": 2, "categoria": "Ropa"},
        3: {"nombre": "Manzanas", "precio": 1000, "stock": 1, "categoria": "Alimentos"},
    }
    test_ventas = [
        {"nombre": "Laptop", "cantidad": 2, "total": 1500000, "id_producto": 1},
        {"nombre": "Camiseta", "cantidad": 1, "total": 15000, "id_producto": 2},
    ]
    
    print("=== Prueba de mostrar_resumen_inventario ===")
    mostrar_resumen_inventario(test_productos)
    
    print("\n=== Prueba de mostrar_reporte_ventas ===")
    mostrar_reporte_ventas(test_ventas)
    
    print("\n=== Prueba de generar_alerta_stock_bajo ===")
    generar_alerta_stock_bajo(test_productos)
```

### 5. Módulo Principal (`main.py`)

El líder técnico ya ha desarrollado el esqueleto del programa principal. Tu tarea es completarlo, integrando las funciones de los módulos anteriores para que el programa funcione correctamente.

**Requisitos del `main.py`**:

1.  **Importar módulos**: Debes importar todas las funciones necesarias desde `validador.py`, `gestion_inventario.py`, `procesamiento_ventas.py` y `reportes.py`.

2.  **Menú Principal**: El programa debe mostrar un menú con las siguientes opciones:
    ```
    === SISTEMA DE GESTIÓN DE INVENTARIO ===
    1. Ver Inventario
    2. Buscar Producto por Nombre
    3. Filtrar Productos por Categoría
    4. Registrar Venta
    5. Ver Reporte de Ventas
    6. Ver Resumen del Inventario
    7. Generar Alerta de Stock Bajo
    8. Salir
    ```

3.  **Funcionalidad de cada opción**:
    - **Opción 1**: Muestra el inventario completo usando `mostrar_inventario()`.
    - **Opción 2**: Solicita un nombre al usuario, usa `buscar_producto_por_nombre()` para encontrarlo y muestra los datos del producto si existe, o un mensaje de "No encontrado".
    - **Opción 3**: Pide una categoría al usuario, usa `filtrar_por_categoria()` y muestra los productos encontrados.
    - **Opción 4**: Registra una venta.
        - Debe mostrar el inventario para que el usuario vea los IDs.
        - Solicita el ID del producto y la cantidad, usando `validar_opcion()`.
        - Llama a `registrar_venta()`.
        - Muestra un mensaje de éxito o fracaso según corresponda.
    - **Opción 5**: Muestra el reporte de ventas usando `mostrar_reporte_ventas()`.
    - **Opción 6**: Muestra el resumen del inventario usando `mostrar_resumen_inventario()`.
    - **Opción 7**: Genera la alerta de stock bajo usando `generar_alerta_stock_bajo()`.
    - **Opción 8**: Muestra el mensaje "¡Hasta pronto!" y termina el programa.

4.  **Validaciones**:
    - Todas las entradas del usuario (IDs, cantidades, nombres) deben ser validadas con `validar_opcion()` del módulo `validador.py` cuando corresponda.
    - El menú debe usar un bucle que se repita hasta que el usuario seleccione la opción "Salir".

**Recuerda**: Debes crear los archivos `inventario.py` y `ventas.py` con los datos iniciales para que `main.py` pueda importarlos y usarlos.

## Criterios de Evaluación (Rúbrica)

1.  **Crea y manipula variables y estructuras de datos, considerando su tipo.** (1 punto)
    - Uso correcto de diccionarios y listas para representar productos y ventas.
    - Conversión de tipos y manejo de datos.

2.  **Crea funciones con diferentes tipos de variables y parámetros, considerando las buenas prácticas.** (3 puntos)
    - Las funciones están correctamente definidas y utilizan parámetros y retornos de manera adecuada.
    - Se aplica el principio de responsabilidad única (una función hace una cosa).
    - Docstrings y comentarios en el código.

3.  **Modulariza programas en Python, utilizando adecuadamente estructuras de archivos.** (3 puntos)
    - Los módulos (`validador.py`, `gestion_inventario.py`, etc.) están correctamente definidos e importados en `main.py`.
    - Separación clara de responsabilidades entre los archivos.

4.  **Valida adecuadamente tipos de datos, funciones y programas, probándolos adecuadamente y verificando las salidas correspondientes.** (3 puntos)
    - Los `if __name__ == '__main__':` contienen los tests requeridos.
    - Las validaciones de entrada (`validar_opcion`) funcionan correctamente.
    - El programa maneja errores (stock insuficiente, producto no encontrado, etc.) de manera elegante.

## Consideraciones y Recomendaciones

- **Formato de entrega**: Crea un repositorio que contenga todos los scripts (`.py`), incluyendo `inventario.py` y `ventas.py` con datos iniciales en una rama llamada `develop`. Sube tu respuesta en GitHub.

- **Buenas prácticas**: Recuerda usar nombres descriptivos para variables y funciones. Mantén la indentación correcta (4 espacios). Agrega comentarios donde sea necesario para explicar la lógica.

- **Pruebas**: Ejecuta y verifica los tests proporcionados en cada módulo (usando el `if __name__ == '__main__'`) antes de integrar todo en `main.py`. Asegúrate de que todas las funcionalidades funcionen como se espera.

- **Datos de prueba**: Crea un inventario inicial con al menos 6 productos de diferentes categorías para probar las funcionalidades de filtrado y reportes.

- **Manejo de errores**: Si bien el programa valida las entradas, considera situaciones como:
    - Intentar vender más de lo que hay en stock.
    - Buscar un producto que no existe.
    - Ingresar un valor no numérico donde se espera un número (manejado por `validar_opcion`).

¡Mucho éxito!