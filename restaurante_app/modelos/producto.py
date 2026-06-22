class Producto:
    """Clase que representa un producto (plato, bebida, etc.) del restaurante"""

    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        """Constructor: inicializa los datos del producto"""
        self.codigo = codigo        # Código único de identificación
        self.nombre = nombre        # Nombre del producto
        self.precio = precio        # Precio de venta
        self.categoria = categoria  # Ej: Entrada, Plato fuerte, Bebida, Postre

    def __str__(self) -> str:
        """Representación legible del producto"""
        return f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"