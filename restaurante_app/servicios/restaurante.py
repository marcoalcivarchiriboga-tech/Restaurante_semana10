from modelos.producto import Producto

class RestauranteServicio:
    def __init__(self, productos_iniciales: list = None):
        self.productos = productos_iniciales if productos_iniciales is not None else []

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False # Ya existe
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nuevo_precio: float, nueva_categoria: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            producto.categoria = nueva_categoria
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def obtener_todos(self) -> list:
        return self.productos
    

