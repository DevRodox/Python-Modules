class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def surtir_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.cantidad += cantidad
                break

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"{producto.nombre}: {producto.cantidad}")
