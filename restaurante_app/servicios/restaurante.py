from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio: administra los productos y clientes del restaurante"""

    def __init__(self, nombre: str):
        """Constructor: define el nombre y crea listas vacías"""
        self.nombre = nombre
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto al menú"""
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        """Registra un nuevo cliente en el sistema"""
        self.clientes.append(cliente)

    def mostrar_menu(self) -> None:
        """Muestra todos los productos disponibles"""
        print(f"\n📋 Menú de {self.nombre}")
        if not self.productos:
            print("No hay productos registrados.")
            return
        for item in self.productos:
            print(f"- {item}")

    def mostrar_clientes(self) -> None:
        """Muestra todos los clientes registrados"""
        print(f"\n👥 Clientes registrados en {self.nombre}")
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for persona in self.clientes:
            print(f"- {persona}")