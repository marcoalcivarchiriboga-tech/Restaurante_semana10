from modelos.producto import Producto

from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tipo_de_envase: str) -> None:
        # Asegúrate de que el orden aquí coincida con el __init__ de Producto
        super().__init__(codigo, nombre, precio, categoria) 
        self.tipo_de_envase = tipo_de_envase

    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base}, Tipo de envase: {self.tipo_de_envase}"

    def a_diccionario(self) -> dict:
        """Sobrescribe el método del padre para incluir el envase al guardar en JSON"""
        # 1. Obtenemos el diccionario base de la clase Producto
        datos = super().a_diccionario()
        
        # 2. Le agregamos la información específica de la Bebida
        datos["tipo_de_envase"] = self.tipo_de_envase
        
        # Opcional pero recomendado: Añadir un "tipo" te ayudará al cargar el JSON
        # para saber si debes reconstruir un Producto normal o una Bebida
        datos["tipo_producto"] = "Bebida" 
        
        return datos