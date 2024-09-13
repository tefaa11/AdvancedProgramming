import os
from abc import ABC, abstractmethod


class TiendaAbstracta(ABC):
    @abstractmethod
    def menu_principal(self):
        pass


class Tienda(TiendaAbstracta):
    def __init__(self):
        self.categorias = {
            1: "Celulares",
            2: "Computadores",
            3: "Televisores",
            4: "Consolas de videojuego",
        }
        self.productos_categoria = {
            "Celulares": {
                1: {"nombre": "Samsung S24 ultra", "precio": 4400000},
                2: {"nombre": "Iphone 15 pro max", "precio": 4250000},
                3: {"nombre": "Xiaomi 14 ultra", "precio": 4220000},
            },
            "Computadores": {
                1: {"nombre": "HP x360 convertible", "precio": 4700000},
                2: {"nombre": "MacBook Air 15", "precio": 7000000},
                3: {"nombre": "HP x360 convertible", "precio": 4700000},
            },
            "Televisores": {
                1: {"nombre": "Sony 4k", "precio": 1300000},
                2: {"nombre": "Samsung QLED", "precio": 1700000},
                3: {"nombre": "LG OLED", "precio": 1500000},
            },
            "Consolas de videojuego": {
                1: {"nombre": "PlayStation 5", "precio": 3500000},
                2: {"nombre": "Xbox Series x", "precio": 3200000},
                3: {"nombre": "Nintendo Switch", "precio": 2500000},
            },
        }
        self.carrito = []

    def get_categorias(self):
        return self.categorias

    def get_productos_categoria(self):
        return self.productos_categoria

    def get_carrito(self):
        return self.carrito

    def set_carrito(self, carrito):
        self.carrito = carrito

    def menu_principal(self):
        print("MENU")
        print("1. Agregar producto al carrito")
        print("2. Eliminar producto del carrito")
        print("3. Pagar")
        print("4. Salir")

    def menu_categorias(self):
        print("Seleccione una categoria: ")
        for i, categoria in self.get_categorias().items():
            print(f"{i}. {categoria}")

    def productos(self, categoria):
        print(f"Productos en la categoria: {categoria}")
        for i, producto in self.get_productos_categoria()[categoria].items():
            print(f"{i}. {producto['nombre']} - {producto['precio']}")

    def agregar_producto(self, categoria, producto_index):
        if categoria in self.get_productos_categoria():
            productos = list(self.get_productos_categoria()[categoria].values())
            if producto_index > 0 and producto_index <= len(productos):
                self.get_carrito().append(
                    {"Categoria": categoria, "Producto": productos[producto_index - 1]}
                )
                print(f"{productos[producto_index - 1]['nombre']} agregado al carrito")
            else:
                print("Ingrese un número valido")
                producto_index = int(input("Ingrese un producto: "))
                self.agregar_producto(categoria, producto_index)

    def eliminar(self):
        if len(self.get_carrito()) > 0:
            print("Productos en el carrito:")
            for i, producto in enumerate(self.get_carrito()):
                print(
                    f"{i+1}. {producto['Categoria']} - {producto['Producto']['nombre']}"
                )
            eliminar = int(input("Ingrese el número del producto que desea eliminar: "))
            if eliminar > 0 and eliminar <= len(self.get_carrito()):
                del self.get_carrito()[eliminar - 1]
                print("Producto eliminado")
            else:
                print("Ingrese un número valido")
                self.eliminar()
        else:
            print("No hay productos en el carrito")

    def pagar(self):
        if len(self.get_carrito()) > 0:
            monto_total = 0
            for producto in self.get_carrito():
                monto_total += producto["Producto"]["precio"]
            print(f"Monto total: {monto_total} COP")
            print("¿Desea pagar?")
            print("1. Si")
            print("2. No")
            respuesta = input("Ingrese una opción: ")
            if respuesta == "1":
                nombre = input("Ingrese su nombre: ")
                while not nombre.isalpha():
                    print("Nombre invalido, debe ser alfabetico")
                    nombre = input("Ingrese su nombre: ")
                documento = input("Ingrese su documento: ")
                while not documento.isdigit():
                    print("Documento invalido, debe ser numerico")
                    documento = input("Ingrese su documento: ")
                tarjeta = input("Ingrese su numero de tarjeta: ")
                while not tarjeta.isdigit():
                    print("Tarjeta invalida, debe ser numerica")
                    tarjeta = input("Ingrese su tarjeta: ")
                direccion = input("Ingrese su direccion: ")
                self.set_carrito([])
            elif respuesta == "2":
                print("Compra cancelada")
            else:
                print("Opción invalida")
                self.pagar()
        else:
            print("No hay productos en el carrito")


# inicio
tienda = Tienda()
print("-----¡Bienvenido a nuestra tienda de tecnología!-----")
while True:
    tienda.menu_principal()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        tienda.menu_categorias()
        categoria = int(input("Ingrese una categoria: "))
        if categoria > 0 and categoria <= len(tienda.get_categorias()):
            cat_seleccionada = list(tienda.get_categorias().values())[categoria - 1]
            tienda.productos(cat_seleccionada)
            producto_index = int(input("Ingrese un producto: "))
            if producto_index > 0 and producto_index <= len(
                tienda.get_productos_categoria()[cat_seleccionada]
            ):
                tienda.agregar_producto(cat_seleccionada, producto_index)
            else:
                print("Ingrese un número valido")
                producto_index = int(input("Ingrese un producto: "))
                tienda.agregar_producto(cat_seleccionada, producto_index)
        else:
            print("Ingrese un número valido: ")
            categoria = int(input("Ingrese una categoria: "))
            cat_seleccionada = list(tienda.get_categorias().values())[categoria - 1]
            tienda.productos(cat_seleccionada)
            producto_index = int(input("Ingrese un producto: "))
            tienda.agregar_producto(cat_seleccionada, producto_index)
    elif opcion == "2":
        tienda.eliminar()
    elif opcion == "3":
        tienda.pagar()
    elif opcion == "4":
        print("-----¡Gracias por visitarnos!-----")
        break
    else:
        print("Opción invalida")
