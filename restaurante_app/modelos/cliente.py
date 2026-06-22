class Cliente:
    """Clase que representa a un cliente del restaurante"""

    def __init__(self, id_cliente: str, nombre: str, telefono: str = ""):
        """Constructor: inicializa los datos del cliente"""
        self.id_cliente = id_cliente  
        self.nombre = nombre           
        self.telefono = telefono       

    def __str__(self) -> str:
        """Representación legible del cliente"""
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Teléfono: {self.telefono or 'Sin registrar'}"