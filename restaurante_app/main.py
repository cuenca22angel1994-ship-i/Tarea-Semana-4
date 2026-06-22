from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta el flujo del programa"""
    
    mi_restaurante = Restaurante(nombre="Sabor Casero")

    p1 = Producto(codigo="E01", nombre="Ensalada de manzana", precio=2.50, categoria="Entrada")
    p2 = Producto(codigo="P01", nombre="Costilla asada", precio=7.50, categoria="Plato fuerte")
    p3 = Producto(codigo="B01", nombre="Jugo de naranja", precio=2.00, categoria="Bebida")

    mi_restaurante.agregar_producto(p1)
    mi_restaurante.agregar_producto(p2)
    mi_restaurante.agregar_producto(p3)

    # Crear y agregar clientes
    c1 = Cliente(id_cliente="C101", nombre="Luz Armijos", telefono="0987654432")
    c2 = Cliente(id_cliente="C102", nombre="Diego Guaman", telefono="0977456890")
    c3 = Cliente(id_cliente="C103", nombre="Adrian Zapata", telefono="0976432168")

    mi_restaurante.agregar_cliente(c1)
    mi_restaurante.agregar_cliente(c2)
    mi_restaurante.agregar_cliente(c3)

    # Mostrar información en consola
    print("=== SISTEMA DE GESTIÓN DE RESTAURANTE ===")
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()


# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    main()