from pathlib import Path
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import RestauranteServicio

# Tupla con la información del restaurante
INFO_RESTAURANTE = (
    "EL BUEN SABOR",
    "RUC: 0704640804001",
    "Dirección: Sixto Durán Ballén y Teresa Arcaya",
    "Teléfono: 0991476301"
)

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Registrar bebida"),
    ("3", "Buscar producto/bebida"),
    ("4", "Actualizar producto/bebida"),
    ("5", "Eliminar producto/bebida"),
    ("6", "Listar todos los productos"),
    ("7", "Registrar cliente (Usuario)"),
    ("8", "Buscar cliente"),
    ("9", "Actualizar cliente"),
    ("10", "Eliminar cliente"),
    ("11", "Listar clientes"),
    ("0", "Salir")
)

def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()

def mostrar_menu() -> None:
    print("\n" + "="*50)
    print(f"{INFO_RESTAURANTE[0].center(50)}")
    print("-" * 50)
    print(f"  {INFO_RESTAURANTE[1]}")
    print(f"  {INFO_RESTAURANTE[2]}")
    print(f"  {INFO_RESTAURANTE[3]}")
    print("="*50)
    print(" MENÚ DE OPCIONES ".center(50, "*"))
    print("="*50)
    for numero, descripcion in OPCIONES_MENU:
        print(f"  {numero}. {descripcion}")

def guardar_cambios(restaurante: RestauranteServicio, archivo_servicio: ArchivoServicio) -> None:
    """Convierte los objetos a diccionarios y guarda en el JSON."""
    lista_diccionarios = []
    # Dependiendo de tu implementación de obtener_todos()
    for p in restaurante.obtener_todos():
        lista_diccionarios.append(p.a_diccionario())
        
    guardado = archivo_servicio.guardar_datos(lista_diccionarios)
    if not guardado:
        print("Los cambios no pudieron guardarse en el archivo.")

# --- FUNCIONES DE MENÚ PARA PRODUCTOS ---

def registrar_producto(restaurante: RestauranteServicio, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Producto ---")
    codigo = pedir_texto("Código: ")
    titulo = pedir_texto("Nombre del plato: ")
    try:
        precio = float(pedir_texto("Precio: "))
        categoria = pedir_texto("Categoría: ")
        
        producto = Producto(codigo, titulo, precio, categoria)
        registrado = restaurante.registrar_producto(producto)
        
        if registrado:
            print("Producto registrado correctamente.")
            guardar_cambios(restaurante, archivo_servicio)
        else:
            print("El código ya se encuentra registrado.")
    except ValueError as e:
        print(f"Error: {e} - Asegúrese de ingresar un número válido para el precio.")

def registrar_bebida(restaurante: RestauranteServicio, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Bebida ---")
    codigo = pedir_texto("Código: ")
    titulo = pedir_texto("Nombre de la bebida: ")
    try:
        precio = float(pedir_texto("Precio: "))
        categoria = pedir_texto("Categoría: ")
        tipo_envase = pedir_texto("Tipo de envase (ej. Lata, Vidrio): ")
        
        bebida = Bebida(codigo, titulo, categoria, precio, tipo_envase)
        registrado = restaurante.registrar_producto(bebida) # Suponiendo que el servicio maneja ambos
        
        if registrado:
            print("Bebida registrada correctamente.")
            guardar_cambios(restaurante, archivo_servicio)
        else:
            print("El código ya se encuentra registrado.")
    except ValueError as e:
        print(f"Error: {e} - Asegúrese de ingresar un número válido para el precio.")

def buscar_producto(restaurante: RestauranteServicio) -> None:
    print("\n--- Buscar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    producto = restaurante.buscar_producto(codigo)
    
    if producto is None:
        print("Producto no encontrado.")
    else:
        # Esto usará __str__ o mostrar_informacion() dependiendo de cómo lo llames
        if hasattr(producto, 'mostrar_informacion'):
            print(producto.mostrar_informacion())
        else:
             print(producto)

def listar_productos(restaurante: RestauranteServicio) -> None:
    print("\n--- Listar Productos ---")
    productos = restaurante.obtener_todos()
    if not productos:
        print("No hay productos registrados en el menú.")
    for p in productos:
        if hasattr(p, 'mostrar_informacion'):
            print(p.mostrar_informacion())
        else:
            print(p)

# --- (Las funciones de Actualizar y Eliminar Producto irían aquí siguiendo el mismo patrón) ---
# --- (Las funciones para Usuarios/Clientes irían aquí) ---

# --- FUNCIÓN PRINCIPAL Y BUCLE ---

def ejecutar_menu() -> None:
    # 1. Configuración de persistencia
    ruta_base = Path(__file__).resolve().parent
    ruta_productos = ruta_base / "datos" / "productos.json"
    ruta_productos.parent.mkdir(parents=True, exist_ok=True)
    
    archivo_servicio = ArchivoServicio(str(ruta_productos))
    
    # 2. Carga inicial (necesitarás adaptar tu lógica de carga para diferenciar Producto vs Bebida
    # si guardaste el "tipo_producto" en el JSON como sugerí antes). 
    # Por ahora, simularemos que RestauranteServicio hace esto en su __init__ o en un método de carga.
    restaurante = RestauranteServicio()
    
    # 3. El Despachador de Opciones
    opciones = {
        "1": lambda: registrar_producto(restaurante, archivo_servicio),
        "2": lambda: registrar_bebida(restaurante, archivo_servicio),
        "3": lambda: buscar_producto(restaurante),
        # "4": lambda: actualizar_producto(restaurante, archivo_servicio),
        # "5": lambda: eliminar_producto(restaurante, archivo_servicio),
        "6": lambda: listar_productos(restaurante),
        # Los lambdas de cliente (Usuario) irían aquí asociados al 7, 8, 9, 10 y 11
    }
    
    print(f"Opciones disponibles: {', '.join(opciones.keys())}, y 0 para salir.")
    
    while True:
        mostrar_menu()
        seleccion = pedir_texto("Seleccione una opción: ")
        
        if seleccion == "0":
            print("Cerrando el sistema del restaurante...")
            break
            
        elif seleccion in opciones:
            # Se ejecuta la función asociada al número
            opciones[seleccion]()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
    