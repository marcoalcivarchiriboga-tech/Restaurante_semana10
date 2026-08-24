import json

class ArchivoServicio:
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def cargar_datos(self) -> list:
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Aviso: productos.json todavía no existe. Se iniciará con una colección vacía.")
            return []
        except json.JSONDecodeError:
            print("Error: El contenido del archivo no posee un formato JSON válido. Iniciando vacío.")
            return []
        except PermissionError:
            print("Error: No existen permisos suficientes para leer el archivo.")
            return []

    def guardar_datos(self, datos: list) -> bool:
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4)
            return True
        except PermissionError:
            print("Error: No existen permisos suficientes para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")
            return False
        