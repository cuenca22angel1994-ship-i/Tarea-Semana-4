# Sistema de Gestión de Restaurante (`restaurante_app`)

Este proyecto es una aplicación de consola básica desarrollada en **Python** utilizando el paradigma de **Programación Orientada a Objetos (POO)**. Su propósito es demostrar la correcta modularización de un software mediante la separación de responsabilidades en carpetas y la comunicación fluida entre archivos por medio de importaciones.

## Autor ##
**Estudiante:** Angel Rafael Cuenca Tamayo
**Institución:** Universidad Estatal Amazónica

## Arquitectura del Proyecto ##
1. `modelos/producto.py`
Representa un elemento disponible en el restaurante (plato, bebida, postre, etc.).
- **Atributos**: `codigo`, `nombre`, `precio`, `categoria`
- **Métodos**: Constructor `__init__`, método especial `__str__` para mostrar información en formato legible.

2. `modelos/cliente.py`
Representa a una persona que visita o consume en el restaurante.
- **Atributos**: `id_cliente`, `nombre`, `telefono`
- **Métodos**: Constructor `__init__`, método especial `__str__`.

3. `servicios/restaurante.py`
Clase encargada de administrar los productos y clientes del sistema.
- **Atributos**: `nombre`, lista de productos, lista de clientes
- **Métodos**:
  - `agregar_producto()`: Registra un nuevo producto
  - `agregar_cliente()`: Registra un nuevo cliente
  - `mostrar_menu()`: Muestra todos los productos disponibles
  - `mostrar_clientes()`: Muestra la lista de clientes registrados

## ¿Cómo ejecutar el programa? ##
1. Descarga o clona el repositorio en tu computadora
2. Abre una terminal y dirígete a la carpeta raíz `restaurante_app`
3. Ejecuta el archivo principal con el comando:
   ```bash
   python main.py
