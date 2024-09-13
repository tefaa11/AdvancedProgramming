import os

categorias = {
    1: "Celulares",
    2: "Computadores",
    3: "Televisores",
    4: "Consolas de videojuego",
}

productos_categoria = {
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

carrito = []


def menu_principal():
    print("MENU")
    print("1. Agregar producto al carrito")
    print("2. Eliminar producto del carrito")
    print("3. Pagar")
    print("4. Salir")

def menu_categorias():
    print("Seleccione una categoria:")
    for i, categoria in categorias.items():
        print(f"{i}. {categoria}")

def productos(categorias):
    print(f"Productos en la categoria:{categoria}")
    for i, producto in productos_categoria[categoria].items():
        print(f"{i}. {producto["nombre"]}-{producto["precio"]} COP")
        }

def agregar_producto():
    if categoria in productos_categoria:
        productos = list(productos_categoria[categoria].values())
        if producto_i