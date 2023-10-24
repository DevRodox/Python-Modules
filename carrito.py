class ItemCarrito:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class CarritoCompras:
    def __init__(self):
        self.items = []

    def agregar_producto(self, item):
        self.items.append(item)

    def eliminar_producto(self, nombre_producto):
        self.items = [item for item in self.items if item.nombre != nombre_producto]

    def ver_productos(self):
        for item in self.items:
            print(f"{item.nombre}: {item.cantidad}")