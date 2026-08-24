class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio) # Se espera un valor numérico
        self.categoria = categoria

    def a_diccionario(self) -> dict:
        """Convierte la información del objeto a un diccionario para JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }
    
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} ({self.categoria})"
    