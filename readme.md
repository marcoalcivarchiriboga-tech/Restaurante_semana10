# Sistema de Gestión para Restaurante (`restaurante_app`)

Aplicación desarrollada en **Python** orientada a consola, diseñada bajo los paradigmas de la **Programación Orientada a Objetos (POO)** y los principios **SOLID**. El sistema permite administrar de forma eficiente el catálogo unificado de productos y bebidas del restaurante, así como el registro de los clientes recurrentes.

## Información del Estudiante
**Nombre Completo:** Marco Julio Alcívar Chiriboga 
**Asignatura:** Programación Orientada a Objetos (Semana 8)
**Institución:** Universidad Estatal Amazónica

## Arquitectura y Estructura Modular

El proyecto se encuentra estrictamente modularizado para separar las responsabilidades de datos, lógica de negocio e interacción con el usuario:

```text
restaurante_app/
|
├── datos/
│   └── productos.json         # Archivo físico para la persistencia de datos (JSON)
|
├── modelos/
│   ├── __init__.py        # Inicializador del paquete de modelos
│   ├── producto.py        # Clase base para la gestión de productos generales
│   ├── bebida.py          # Clase hija que hereda de Producto (Herencia y Polimorfismo)
│   └── usuario.py         # Clase independiente para representar a los usuarios/clientes
|
├── servicios/
│   ├── __init__.py        # Inicializador del paquete de servicios
│   ├── archivo_servicio.py # Servicio responsable de la lectura y escritura del JSON
│   └── restaurante.py     # Capa encargada de las colecciones en memoria y reglas de negocio
|
├── main.py                # Punto de arranque, menú interactivo y controlador principal
└── README.md              # Documentación oficial y explicación de la arquitectura

Componentes y Principios Aplicados
1. Modelos de Datos (modelos/)
Producto (producto.py): Define la estructura base de los artículos del restaurante. Contiene atributos comunes como código, nombre, categoría y precio, además del método fundamental mostrar_informacion().

Bebida (bebida.py): Aplica herencia al extender de la clase Producto. Incorpora un atributo propio (tipo_envase) y aplica polimorfismo al sobrescribir mostrar_informacion() para complementar los datos heredados sin alterar la lógica general (Principio de Sustitución de Liskov).

Cliente (cliente.py): Modela la información personal del cliente (identificación, nombre y correo) manteniendo total independencia de la jerarquía de productos (Principio de Responsabilidad Única).

2. Capa de Servicios (servicios/)
Restaurante (restaurante.py): Actúa como el motor logístico de la aplicación. Administra una colección unificada de productos (donde conviven objetos tipo Producto y Bebida de manera transparente) y una lista independiente de clientes.

Incluye validaciones robustas para evitar duplicidad de códigos en productos/bebidas e identificaciones repetidas en los clientes.

3. Interfaz de Usuario (main.py)
Gestiona un bucle interactivo basado en consola impulsado por opciones numéricas (input()). Se encarga exclusivamente de capturar datos, instanciar objetos, invocar los métodos del servicio Restaurante y presentar los resultados formateados en pantalla.

Principios SOLID Implementados
S (Responsabilidad Única): Cada archivo y clase posee un propósito específico (las clases de modelos gestionan sus propios datos, el servicio administra colecciones y main.py maneja la interfaz).

O (Abierto/Cerrado): La clase Bebida amplía el comportamiento del sistema mediante herencia y polimorfismo sin necesidad de reescribir la lógica central del servicio.

L (Sustitución de Liskov): Los objetos de la clase derivada (Bebida) pueden utilizarse indistintamente en la colección de productos genéricos sin generar errores ni requerir validaciones repetitivas de tipo (isinstance).

# Semana 9
## Aplicacion de Estructuras de Datos 

| Estructura | Tipo en Python | Aplicacion en el Proyecto |
| **Listas** | list | Utilizadas para administrar las colecciones dinámicas de productos (`self.productos) y clientes (`self.clientes`). permiten realizar operaciones de registro, busqueda, actualizacion, eliminacion y listado.|
|**Tuplas** | `tuple` | Utilizadas para manejar informacion inmutable que debe mantenerse estable durante la ejecucion, como la tupla con la información general del negocio (nombre, RUC, direccion, teléfono) y las opciones fijas del menú.
| **Diccionarios** | `dict` | Utilizados para establecer relaciones de clave $\rigtarrow$ valor. Se aplica para mapear las opciones numéricas del menú interactivo con sus respectivas funciones de la interfaz de usuario. |
| **Conjuntos** | `set` | Utilizados para gestionar colecciones de elementos unicos sin duplicados. Se aplican en la funcion de obtencion de categorias para extraer y presentar unicamente las categorias unicas de los productosregistrados. | 

# Semana 10: Persistencia de Datos y Manejo de Excepciones

En esta etapa de desarrollo, el sistema evoluciona para incluir almacenamiento persistente mediante archivos JSON. Esto garantiza que el catálogo de productos y bebidas del restaurante "El Buen Sabor" no se pierda al cerrar la aplicación. Además, se incorpora un robusto manejo de excepciones para prevenir cierres inesperados.

### Nuevos Componentes y Modificaciones
* **`datos/productos.json`**: Archivo físico utilizado como medio de almacenamiento de la colección.
* **`servicios/archivo_servicio.py`**: Nuevo módulo de servicio dedicado exclusivamente a la lectura (`json.load()`) y escritura (`json.dump()`) del archivo. Cumple con el Principio de Responsabilidad Única al separar la persistencia de la lógica de negocio.
* **`modelos/producto.py` y `bebida.py`**: Se integró el método `a_diccionario()` para serializar los objetos a una estructura compatible con JSON, manteniendo intactos los atributos heredados (como el `tipo_de_envase`).
* **`main.py` (Actualización de Interfaz)**:
  * Se implementó una **tupla constante** (`INFO_RESTAURANTE`) que actúa como encabezado inmutable en la interfaz de consola, mostrando el nombre, RUC, dirección y teléfono.
  * Se expandió el menú a 12 opciones utilizando un despachador dinámico basado en un diccionario y funciones `lambda`, optimizando el flujo de ejecución sin abusar de condicionales `if/elif`.

### Manejo de Excepciones Implementado
El acceso a archivos y la captura de datos están protegidos rigurosamente con bloques `try-except`:
* **`FileNotFoundError`**: Permite que la aplicación inicie de manera controlada con una colección vacía si el archivo `productos.json` todavía no existe.
* **`json.JSONDecodeError`**: Protege la inicialización en caso de que el archivo exista pero su formato interno esté corrupto o no sea un JSON válido.
* **`PermissionError`**: Advierte al usuario de forma amigable si el sistema operativo deniega los permisos de lectura o escritura en el directorio `datos/`.
* **`KeyError`**: Mantiene la estabilidad al reconstruir los objetos durante la fase de carga si algún registro antiguo no posee las claves esperadas.
* **`ValueError`**: Empleado en los formularios de registro de la consola (ej. al pedir el precio) para impedir que el ingreso de letras o caracteres inválidos detenga la aplicación abruptamente.

### Flujo de Ejecución (Carga y Guardado)
1. **Inicio y Carga:** Al iniciar `main.py`, se crea el `ArchivoServicio` y se intenta leer los datos. Cada registro válido recuperado del JSON se utiliza para instanciar nuevamente objetos `Producto` o `Bebida`, los cuales se cargan en la memoria del `RestauranteServicio`.
2. **Operación en Memoria:** El sistema interactúa con el usuario trabajando netamente con los objetos en memoria para garantizar un alto rendimiento.
3. **Guardado Automático:** Inmediatamente después de que el usuario registra, actualiza o elimina un producto con éxito, `main.py` solicita la colección actualizada, los objetos se convierten a lista de diccionarios, y el servicio sobrescribe el archivo físico, manteniendo la información siempre sincronizada.
