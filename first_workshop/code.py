"""
14/09/2024  - Advanced programming workshop #1

This program is an electronic store that displays products for purchase.

Author: Carol Stefanya Velasco Rodríguez

"""

from abc import ABC, abstractmethod


class Abstract_Store(ABC):
    """
    Abstract class that defines the behavior of a store.

    This class provides a basic structure for a store, including methods for
    displaying the main menu, adding products to the cart, removing products from
    the cart, and paying for the products in the cart.

    Methods:
        display_main_menu: Displays the main menu of the store.
    """

    @abstractmethod
    def display_main_menu(self):
        """
        Abstract method that displays the main menu of the store.

        This method should be implemented by any concrete subclass of
        AbstractStore. It should display the main menu of the store, including
        options for adding products to the cart, removing products from the cart,
        and paying for the products in the cart.
        """
        pass


class Store(Abstract_Store):
    """
    Concrete class that implements the behavior of a store.

    This class provides a basic implementation of a store, including methods for
    displaying the main menu, adding products to the cart, removing products from
    the cart, and paying for the products in the cart.

    Attributes:
        categories (dict): A dictionary of categories, where each key is a category
            name and each value is a list of products in that category.
        products_by_category (dict): A dictionary of products, where each key is a
            product name and each value is a dictionary of product attributes.
        cart (list): A list of products in the cart.

    Methods:
        get_categories: Returns the categories of the store.
        get_products_by_category: Returns the products of each category.
        get_cart: Returns the cart of the store.
        set_cart: Sets the cart of the store.
        display_main_menu: Displays the main menu of the store.
        display_categories: Displays the categories of the store.
        display_products: Displays the products of a category.
        add_product: Adds a product to the cart.
        remove_product: Removes a product from the cart.
        pay: Pays for the products in the cart.
        view_cart: Displays the products in the cart.
        search_by_brand: Searches for products by brand.
        search_by_price: Searches for products by price.
    """

    def __init__(self):
        """
        Initializes the store with categories and products.

        This method initializes the store with a set of categories and products.
        It also initializes the cart as an empty list.
        """
        self.categories = {
            1: "Celulares",
            2: "Computadores",
            3: "Televisores",
            4: "Consolas de videojuego",
            5: "Accesorios electrónicos",
        }
        self.products_by_category = {
            "Celulares": {
                1: {
                    "nombre": "Samsung S24 ultra",
                    "precio": 4400000,
                    "marca": "Samsung",
                },
                2: {"nombre": "Iphone 15 pro max", "precio": 4250000, "marca": "Apple"},
                3: {"nombre": "Xiaomi 14 ultra", "precio": 4220000, "marca": "Xiaomi"},
            },
            "Computadores": {
                1: {"nombre": "HP x360 convertible", "precio": 4700000, "marca": "HP"},
                2: {"nombre": "MacBook Air 15", "precio": 7000000, "marca": "Apple"},
                3: {"nombre": "HP x360 convertible", "precio": 4700000, "marca": "HP"},
            },
            "Televisores": {
                1: {"nombre": "Sony 4k", "precio": 1300000, "marca": "Sony"},
                2: {"nombre": "Samsung QLED", "precio": 1700000, "marca": "Samsung"},
                3: {"nombre": "LG OLED", "precio": 1500000, "marca": "LG"},
            },
            "Consolas de videojuego": {
                1: {"nombre": "PlayStation 5", "precio": 3500000, "marca": "Sony"},
                2: {"nombre": "Xbox Series x", "precio": 3200000, "marca": "Microsoft"},
                3: {
                    "nombre": "Nintendo Switch",
                    "precio": 2500000,
                    "marca": "Nintendo",
                },
            },
            "Accesorios electrónicos": {
                1: {"nombre": "Cargador USB-C", "precio": 50000, "marca": "Motorola"},
                2: {
                    "nombre": "Auriculares inalámbricos",
                    "precio": 150000,
                    "marca": "Sony",
                },
                3: {"nombre": "Batería portátil", "precio": 200000, "marca": "HP"},
            },
        }
        self.cart = []

    def get_categories(self):
        """
        Returns the categories of the store.

        This method returns a dictionary of categories, where each key is a category
        name and each value is a list of products in that category.

        Returns:
            dict: A dictionary of categories.
        """
        return self.categories

    def get_products_by_category(self):
        """
        Returns the products of each category.

        This method returns a dictionary of products, where each key is a product
        name and each value is a dictionary of product attributes.

        Returns:
            dict: A dictionary of products.
        """
        return self.products_by_category

    def get_cart(self):
        """
        Returns the cart of the store.

        This method returns a list of products in the cart.

        Returns:
            list: A list of products in the cart.
        """
        return self.cart

    def set_cart(self, cart):
        """
        Sets the cart of the store.

        This method sets the cart of the store to a new list of products.

        Args:
            cart (list): A list of products to set as the cart.
        """
        self.cart = cart

    def display_main_menu(self):
        """
        Displays the main menu of the store.

        This method displays the main menu of the store, including options for
        adding products to the cart, removing products from the cart, and paying
        for the products in the cart.
        """
        print("MENU")
        print("1. Agregar producto al carrito")
        print("2. Eliminar producto del carrito")
        print("3. Pagar")
        print("4. Ver carrito")
        print("5. Buscar por marca")
        print("6. Buscar por precio")
        print("7. Salir")

    def display_categories(self):
        """
        Displays the categories of the store.

        This method displays the categories of the store, including a list of
        products in each category.
        """
        print("Seleccione una categoria: ")
        for i, category in self.get_categories().items():
            print(f"{i}. {category}")

    def display_products(self, category):
        """
        Displays the products of a category.

        This method displays the products of a category, including the product
        name and price.

        Args:
            category (str): The name of the category to display products for.
        """
        print(f"Productos en la categoria: {category}")
        for i, product in self.get_products_by_category()[category].items():
            print(f"{i}. {product['nombre']} - {product['precio']}")

    def add_product(self, category, product_index):
        """
        Adds a product to the cart.

        This method adds a product to the cart, including the product name and
        price.

        Args:
            category (str): The name of the category the product is in.
            product_index (int): The index of the product to add to the cart.
        """
        if category in self.get_products_by_category():
            products = list(self.get_products_by_category()[category].values())
            if product_index > 0 and product_index <= len(products):
                self.get_cart().append(
                    {"Categoria": category, "Producto": products[product_index - 1]}
                )
                print(f"{products[product_index - 1]['nombre']} agregado al carrito")
            else:
                print("Ingrese un número valido")
                product_index = int(input("Ingrese un producto: "))
                self.add_product(category, product_index)

    def remove_product(self):
        """
        Removes a product from the cart.

        This method removes a product from the cart, including the product name
        and price.
        """
        if len(self.get_cart()) > 0:
            print("Productos en el carrito:")
            for i, product in enumerate(self.get_cart()):
                print(
                    f"{i+1}. {product['Categoria']} - {product['Producto']['nombre']}"
                )
            remove = int(input("Ingrese el número del producto que desea eliminar: "))
            if remove > 0 and remove <= len(self.get_cart()):
                del self.get_cart()[remove - 1]
                print("Producto eliminado")
            else:
                print("Ingrese un número valido")
                self.remove_product()
        else:
            print("No hay productos en el carrito")

    def pay(self):
        """
        Pays for the products in the cart.

        This method pays for the products in the cart, including the total price
        and payment information.
        """
        if len(self.get_cart()) > 0:
            total_amount = 0
            for product in self.get_cart():
                total_amount += product["Producto"]["precio"]
            print(f"Monto total: {total_amount} COP")
            print("¿Desea pagar?")
            print("1. Si")
            print("2. No")
            response = input("Ingrese una opción: ")
            if response == "1":
                name = input("Ingrese su nombre: ")
                while not name.isalpha():
                    print("Nombre invalido, debe ser alfabetico")
                    name = input("Ingrese su nombre: ")
                document = input("Ingrese su documento: ")
                while not document.isdigit():
                    print("Documento invalido, debe ser numerico")
                    document = input("Ingrese su documento: ")
                card = input("Ingrese su numero de tarjeta: ")
                while not card.isdigit():
                    print("Tarjeta invalida, debe ser numerica")
                    card = input("Ingrese su tarjeta: ")
                address = input("Ingrese su direccion: ")
                self.set_cart([])
                print("¡Compra exitosa!")
            elif response == "2":
                print("Compra cancelada")
            else:
                print("Opción invalida")
                self.pay()
        else:
            print("No hay productos en el carrito")

    def view_cart(self):
        """
        Displays the products in the cart.

        This method displays the products in the cart, including the product name
        and price.
        """
        if len(self.get_cart()) > 0:
            print("Productos en el carrito:")
            for i, product in enumerate(self.get_cart()):
                print(
                    f"{i+1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No hay productos en el carrito")

    def search_by_brand(self):
        """
        Searches for products by brand.

        This method searches for products by brand, including the product name and
        price.
        """
        brand = input("Ingrese la marca que desea buscar: ")
        found_products = []
        for category, products in self.get_products_by_category().items():
            for product in products.values():
                if product["marca"].lower() == brand.lower():
                    found_products.append({"Categoria": category, "Producto": product})
        if len(found_products) > 0:
            print("Productos encontrados:")
            for i, product in enumerate(found_products):
                print(
                    f"{i+1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No se encontraron productos con esa marca")

    def search_by_price(self):
        """
        Searches for products by price.

        This method searches for products by price, including the product name and
        price.
        """
        min_price = int(input("Ingrese el precio minimo: "))
        max_price = int(input("Ingrese el precio maximo: "))
        found_products = []
        for category, products in self.get_products_by_category().items():
            for product in products.values():
                if min_price <= product["precio"] <= max_price:
                    found_products.append({"Categoria": category, "Producto": product})
        if len(found_products) > 0:
            print("Productos encontrados:")
            for i, product in enumerate(found_products):
                print(
                    f"{i+1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No se encontraron productos con ese precio")


# inicio
"""
Entry point of the program. Creates a Store instance and starts the main loop.

Attributes:
    store (Store): Technology store instance.

Description:
    This is the main entry point of the program, responsible for managing the store's
    inventory, processing user input, and handling transactions.
"""

store = Store()
print("-----Bienvenido a nuestra tienda de tecnología!-----")

while True:
    store.display_main_menu()
    option = input("Ingresa una opción: ")
    if option == "1":
        store.display_categories()
        category = int(input("Ingresa una categoría: "))
        if category > 0 and category <= len(store.get_categories()):
            selected_category = list(store.get_categories().values())[category - 1]
            store.display_products(selected_category)
            product_index = int(input("Ingresa un producto: "))
            if product_index > 0 and product_index <= len(
                store.get_products_by_category()[selected_category]
            ):
                store.add_product(selected_category, product_index)
            else:
                print("Ingresa un número válido")
                product_index = int(input("Ingresa un producto: "))
                store.add_product(selected_category, product_index)
        else:
            print("Ingresa un número válido")
            category = int(input("Ingresa una categoría: "))
            selected_category = list(store.get_categories().values())[category - 1]
            store.display_products(selected_category)
            product_index = int(input("Ingresa un producto: "))
            store.add_product(selected_category, product_index)
    elif option == "2":
        store.remove_product()
    elif option == "3":
        store.pay()
    elif option == "4":
        store.view_cart()
    elif option == "5":
        store.search_by_brand()
    elif option == "6":
        store.search_by_price()
    elif option == "7":
        print("-----Gracias por visitarnos!-----")
        break
    else:
        print("Opción inválida")
