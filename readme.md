# Sistema de Gestión para Restaurante (`restaurante_app`)

Aplicación desarrollada en **Python** orientada a consola, diseñada bajo los paradigmas de la **Programación Orientada a Objetos (POO)** y los principios **SOLID**. El sistema permite administrar de forma eficiente el catálogo unificado de productos y bebidas del restaurante, así como el registro de los clientes recurrentes.

## Información del Estudiante
**Nombre Completo:** Marco Julio Alcívar Chiriboga 
**Asignatura:** Programación Orientada a Objetos
**Institución:** Universidad Estatal Amazónica

# Sistema de Gestión de Restaurante "El Buen Sabor" (Semana 10)

Proyecto académico en Python para practicar Programación Orientada a Objetos (POO), estructuras de datos, manejo de archivos JSON y manejo de excepciones.

La aplicación administra productos, bebidas y clientes desde la consola. Los productos y bebidas se conservan en un archivo JSON para que sigan disponibles al cerrar y volver a ejecutar el programa.

## Estructura del Proyecto

```text
restaurante_app/
|
|-- datos/
|   `-- productos.json
|
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   |-- bebida.py
|   `-- cliente.py
|
|-- servicios/
|   |-- __init__.py
|   |-- archivo_servicio.py
|   `-- restaurante_servicio.py
|
`-- main.py
```

La carpeta `datos/` no representa una nueva capa de la arquitectura. Solo es la ubicación física donde la aplicación guarda el archivo `productos.json`.

## Ejecución

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

## Responsabilidades

* `modelos/producto.py` : contiene la clase `Producto`, sus validaciones y la conversión simple a diccionario.
* `modelos/bebida.py` : contiene la clase `Bebida` (heredada o específica de productos líquidos) y sus validaciones.
* `modelos/cliente.py` : contiene la clase `Cliente` y sus validaciones principales.
* `servicios/restaurante_servicio.py` : administra las colecciones de productos, bebidas, clientes y pedidos durante la ejecución.
* `servicios/archivo_servicio.py` : lee y escribe los productos y bebidas en formato JSON usando `with open(...)`, `json.load()` y `json.dump()`.
* `main.py` : contiene el menú de consola, crea los servicios, carga los datos iniciales y solicita el guardado cuando cambian los productos o bebidas.

## Persistencia con JSON

Al iniciar la aplicación, `main.py` crea un `ArchivoServicio` y solicita la carga de `datos/productos.json`. Los diccionarios obtenidos desde el archivo se convierten nuevamente en objetos correspondientes, por lo que el resto del sistema sigue trabajando con objetos y no con diccionarios.

Cuando se registra, actualiza o elimina un producto o bebida, la lista actual de objetos se convierte en una lista de diccionarios y se guarda nuevamente en `productos.json`.

Flujo principal:
```text
Inicio de la aplicacion
|
Leer datos/productos.json
|
Convertir diccionarios a objetos
|
Cargar objetos en RestauranteServicio
|
Ejecutar el menu de consola
```

Flujo de guardado:
```text
Operacion sobre productos/bebidas
|
RestauranteServicio modifica la lista en memoria
|
Los objetos se convierten a diccionarios
|
ArchivoServicio actualiza datos/productos.json
```

## Manejo de fallos

El proyecto mantiene `ValueError` para validaciones propias de los modelos, como campos vacíos.

En `ArchivoServicio` se manejan excepciones específicas relacionadas con archivos:

* `FileNotFoundError` : permite iniciar con una lista vacía cuando `productos.json` todavia no existe.
* `json.JSONDecodeError` : informa cuando el archivo existe pero no contiene JSON válido.
* `PermissionError` : informa cuando no existen permisos suficientes para leer o escribir el archivo.

No se utilizan librerías externas ni bases de datos. El objetivo de esta semana es observar una persistencia básica y comprensible usando archivos JSON.

## Uso justificado de las estructuras de datos

El proyecto utiliza `list`, `tuple`, `dict` y `set` en lugares donde cada estructura cumple una responsabilidad concreta dentro del sistema. No se reemplazan las clases por diccionarios, porque esas entidades siguen siendo objetos con atributos, propiedades y validaciones.

### `list`: colecciones de productos, bebidas y clientes
Se utiliza en `servicios/restaurante_servicio.py` para guardar los elementos mientras el programa está en ejecución:

```python
self.productos: list[Producto] = []
self.bebidas: list[Bebida] = []
self.clientes: list[Cliente] = []
```

La lista permite registrar, recorrer, buscar, actualizar, listar y eliminar objetos.

### `tuple`: opciones fijas del menú
Se utiliza en `main.py` para definir las opciones principales del menú. Es apropiado porque esas opciones no necesitan modificarse durante la ejecución.

### `dict`: relación entre claves y valores
Se utiliza en `main.py` para relacionar opciones del menú con funciones, y en `RestauranteServicio` para registrar temporalmente los pedidos durante la ejecución.

### `set`: categorías sin duplicados
Se utiliza para mostrar cada categoría de productos o bebidas una sola vez.

## Menú principal

El programa permite:
1. Registrar producto 
2. Registrar bebida
3. Buscar producto o bebida
4. Actualizar producto o bebida
5. Eliminar producto o bebida
6. Listar todos los productos 
7. Registrar cliente (usuario)
8. Buscar Cliente
9. Actualizar Cliente
10. Eliminar Cliente
11. Listar Cliente
0. Salir

