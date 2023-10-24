from inventario import Inventario, Producto
from carrito import CarritoCompras, ItemCarrito

def menu():
    inventario = Inventario()
    carrito = CarritoCompras()

    while True:
        print("\nMenú:")
        print("1. Agregar Producto al inventario")
        print("2. Surtir Producto al inventario")
        print("3. Mostrar productos del inventario")
        print("4. Agregar producto del inventario al carrito de compras")
        print("5. Eliminar producto del carrito de compras")
        print("6. Ver producto del carrito de compras")
        print("7. Calcular total del carrito de compras")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto a agregar: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            producto = Producto(nombre_producto, cantidad)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a surtir: ")
            cantidad = int(input("Ingrese la cantidad a surtir: "))
            inventario.surtir_producto(nombre_producto, cantidad)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto a agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad a agregar al carrito: "))
            item = ItemCarrito(nombre_producto, cantidad)
            carrito.agregar_producto(item)
        elif opcion == "5":
            nombre_producto = input("Ingrese el nombre del producto a eliminar del carrito: ")
            carrito.eliminar_producto(nombre_producto)
        elif opcion == "6":
            carrito.ver_productos()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()
