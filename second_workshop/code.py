"""
5/10/2024 - Advanced programming workshop #2

This program is an electronic store that displays products for purchase and allows
user registration and login, it is an update to improve the service.

Author: Carol Stefanya Velasco Rodríguez
"""

from abc import ABC, abstractmethod


class StoreUser:
    """
    Class representing a user of the store.

    Attributes:
        username (str): The username of the user, used for logging in.
        password (str): The password associated with the username, used for authentication.
        name (str): The full name of the user, used for display purposes and during transactions.
    """

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name


class Admin(StoreUser):
    """
    Class representing an admin user.

    This class inherits from StoreUser and adds admin-specific functionality.

    Attributes:
        role (str): The role of the user, which is 'admin' for this class.
    """

    def __init__(self, username, password, name):
        super().__init__(username, password, name)
        self.role = "admin"


class User(StoreUser):
    """
    Class representing a regular user.

    This class inherits from StoreUser and adds user-specific functionality.

    Attributes:
        role (str): The role of the user, which is 'user' for this class.
    """

    def __init__(self, username, password, name):
        super().__init__(username, password, name)
        self.role = "user"


class AbstractStore(ABC):
    """
    Abstract class that defines the interface for a store.

    This class serves as a blueprint for any concrete store implementations,
    requiring them to implement specific methods for displaying menus.
    """

    @abstractmethod
    def display_main_menu(self):
        """
        Displays the main menu options for the store.

        This method must be implemented in any subclass of AbstractStore.
        """
        pass


class Store(AbstractStore):
    """
    Concrete class that implements the behavior of a store.

    This class manages categories, products, the shopping cart, user registration,
    and sales processing.

    Attributes:
        categories (dict): A dictionary mapping category IDs to category names.
        products_by_category (dict): A dictionary mapping category names to their corresponding products.
        cart (list): A list containing products that the user has added to their cart.
        users (list): A list of registered users in the store.
        sales (list): A list of completed sales transactions.
    """

    def __init__(self):
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
                3: {"nombre": "Lenovo IdeaPad", "precio": 4500000, "marca": "Lenovo"},
            },
            "Televisores": {
                1: {"nombre": "Sony 4k", "precio": 1300000, "marca": "Sony"},
                2: {"nombre": "Samsung QLED", "precio": 1700000, "marca": "Samsung"},
                3: {"nombre": "LG OLED", "precio": 1500000, "marca": "LG"},
            },
            "Consolas de videojuego": {
                1: {"nombre": "PlayStation 5", "precio": 3500000, "marca": "Sony"},
                2: {"nombre": "Xbox Series X", "precio": 3200000, "marca": "Microsoft"},
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
        self.users = []  # List of registered users
        self.sales = []  # List of completed sales

    def register_user(self, username, password, name, role):
        """
        Registers a new user in the store.

        This method adds a user to the list of registered users,
        distinguishing between regular users and admins based on the role specified.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            name (str): The full name of the new user.
            role (str): The role of the user, which can be either 'admin' or 'user'.
        """
        if role == "admin":
            self.users.append(Admin(username, password, name))
        else:
            self.users.append(User(username, password, name))
        print("Usuario registrado con éxito.")

    def login_user(self, username, password):
        """
        Logs in a user based on provided credentials.

        This method checks the username and password against the registered users
        and returns the user object if the credentials are correct.

        Args:
            username (str): The username of the user attempting to log in.
            password (str): The password of the user attempting to log in.

        Returns:
            StoreUser or None: Returns the user object if credentials are valid,
            otherwise returns None.
        """
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Bienvenido, {user.name}!")
                return user
        print("Credenciales incorrectas.")
        return None

    def get_categories(self):
        """
        Returns the available categories in the store.

        This method provides access to the categories dictionary,
        allowing other methods to retrieve category information.

        Returns:
            dict: A dictionary of categories where keys are category IDs and values are category names.
        """
        return self.categories

    def get_products_by_category(self):
        """
        Returns the products organized by their respective categories.

        This method provides access to the products dictionary,
        allowing other methods to retrieve product information by category.

        Returns:
            dict: A dictionary mapping category names to their respective products.
        """
        return self.products_by_category

    def get_cart(self):
        """
        Returns the current shopping cart.

        This method allows access to the cart attribute,
        which holds the products the user has chosen to purchase.

        Returns:
            list: A list of products currently in the cart.
        """
        return self.cart

    def set_cart(self, cart):
        """
        Updates the shopping cart with the provided list.

        This method is used to modify the cart attribute,
        typically to clear the cart after a successful purchase.

        Args:
            cart (list): The new cart list to be set.
        """
        self.cart = cart

    def display_main_menu(self):
        """
        Displays the main menu options for the store.

        This method prints the available actions a user can take,
        such as adding products to the cart, removing products,
        processing payment, viewing the cart, and searching for products.
        """
        print("MENU")
        print("1. Agregar producto al carrito")
        print("2. Eliminar producto del carrito")
        print("3. Pagar")
        print("4. Ver carrito")
        print("5. Buscar por marca")
        print("6. Buscar por precio")
        print("7. Salir")

    def admin_menu(self):
        """
        Displays the admin menu options.

        This method prints the actions available to admin users,
        such as viewing sales and adding new products to categories.
        """
        print("MENU ADMIN")
        print("1. Ver ventas")
        print("2. Agregar producto a una categoría")
        print("3. Salir")

    def view_sales(self):
        """
        Displays completed sales transactions.

        This method checks if there are any sales recorded and prints
        the details of each sale, including the total amount and buyer's name.
        """
        if not self.sales:
            print("No hay ventas registradas.")
            return
        print("Ventas registradas:")
        for i, sale in enumerate(self.sales):
            print(
                f"{i + 1}. Monto total: {sale['total']} COP, Comprador: {sale['buyer_name']}"
            )

    def add_product_to_category(self):
        """
        Adds a new product to a selected category.

        This method prompts the admin user to select a category and
        then collects the product details (name, price, brand)
        to add it to the specified category.

        Raises:
            ValueError: If the selected category does not exist.
        """
        self.display_categories()
        category_index = int(input("Seleccione el índice de la categoría: ")) - 1
        categories_list = list(self.get_categories().values())

        if category_index < 0 or category_index >= len(categories_list):
            raise ValueError("Categoría no válida.")

        category_name = categories_list[category_index]
        product_name = input("Ingrese el nombre del producto: ")
        product_price = int(input("Ingrese el precio del producto: "))
        product_brand = input("Ingrese la marca del producto: ")

        # Add product to the category
        category_products = self.products_by_category[category_name]
        new_product_id = len(category_products) + 1  # New product ID
        category_products[new_product_id] = {
            "nombre": product_name,
            "precio": product_price,
            "marca": product_brand,
        }
        print(f"Producto {product_name} agregado a la categoría {category_name}.")

    def display_categories(self):
        """
        Displays available categories in the store.

        This method prints all the categories present in the store,
        allowing users to choose where to browse for products.
        """
        print("Categorías disponibles:")
        for i, category in enumerate(self.get_categories().values()):
            print(f"{i + 1}. {category}")

    def display_products(self, category):
        """
        Displays products in the selected category.

        This method retrieves and prints the products available in the specified
        category, including their name and price.

        Args:
            category (str): The name of the category whose products are to be displayed.
        """
        print(f"Productos en la categoría '{category}':")
        for product_id, product in self.products_by_category[category].items():
            print(f"{product_id}. {product['nombre']} - {product['precio']} COP")

    def add_product(self, category, product_index):
        """
        Adds a product to the shopping cart.

        This method retrieves the specified product from the given category
        and adds it to the user's cart.

        Args:
            category (str): The name of the category from which to retrieve the product.
            product_index (int): The index of the product to be added to the cart.
        """
        products = self.products_by_category[category]
        if product_index in products:
            self.cart.append(
                {"Categoria": category, "Producto": products[product_index]}
            )
            print(f"Producto {products[product_index]['nombre']} agregado al carrito.")
        else:
            print("Producto no encontrado.")

    def remove_product(self):
        """
        Removes a product from the shopping cart.

        This method displays the products in the cart,
        allows the user to select one to remove, and updates the cart accordingly.
        """
        if not self.cart:
            print("El carrito está vacío.")
            return

        print("Productos en el carrito:")
        for i, item in enumerate(self.cart):
            print(
                f"{i + 1}. {item['Categoria']} - {item['Producto']['nombre']} - {item['Producto']['precio']}"
            )

        index_to_remove = (
            int(input("Seleccione el índice del producto a eliminar: ")) - 1
        )
        if 0 <= index_to_remove < len(self.cart):
            removed_item = self.cart.pop(index_to_remove)
            print(
                f"Producto {removed_item['Producto']['nombre']} eliminado del carrito."
            )
        else:
            print("Índice no válido.")

    def complete_sale(self):
        """
        Processes the final sale transaction.

        This method prompts the user for their personal information (name, document ID,
        card number, and address) to complete the purchase. It calculates the total amount
        in the cart and records the transaction in the sales list.

        Raises:
            ValueError: If the cart is empty at the time of checkout.
        """
        if not self.cart:
            raise ValueError("El carrito está vacío. No se puede realizar la compra.")

        total_amount = sum(item["Producto"]["precio"] for item in self.cart)
        buyer_name = input("Ingrese su nombre: ")
        document_id = input("Ingrese su documento de identidad: ")
        card_number = input("Ingrese su número de tarjeta: ")
        address = input("Ingrese su dirección: ")

        # Record the sale
        self.sales.append(
            {
                "total": total_amount,
                "buyer_name": buyer_name,
                "document_id": document_id,
                "card_number": card_number,
                "address": address,
            }
        )

        print(f"Compra completada por un total de {total_amount} COP.")
        self.set_cart([])  # Clear the cart after sale

    def view_cart(self):
        """
        Displays the current items in the shopping cart.

        This method checks if there are any products in the cart and prints
        each item along with its category and price. If the cart is empty,
        it notifies the user accordingly.
        """
        if len(self.get_cart()) > 0:
            print("Productos en el carrito:")
            for i, product in enumerate(self.get_cart()):
                print(
                    f"{i + 1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No hay productos en el carrito.")

    def search_by_brand(self):
        """
        Searches for products by brand name.

        This method allows users to input a brand name,
        then iterates through all products to find and display those
        that match the entered brand, regardless of case.

        Raises:
            ValueError: If no products are found for the specified brand.
        """
        brand = input("Ingrese la marca que desea buscar: ")
        found_products = []
        for category, products in self.get_products_by_category().items():
            for product in products.values():
                if product["marca"].lower() == brand.lower():
                    found_products.append({"Categoria": category, "Producto": product})

        if found_products:
            print("Productos encontrados:")
            for i, product in enumerate(found_products):
                print(
                    f"{i + 1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No se encontraron productos con esa marca.")

    def search_by_price(self):
        """
        Searches for products within a specified price range.

        This method prompts the user for minimum and maximum price values,
        then retrieves and displays products whose prices fall within that range.

        Raises:
            ValueError: If no products are found within the specified price range.
        """
        min_price = int(input("Ingrese el precio mínimo: "))
        max_price = int(input("Ingrese el precio máximo: "))
        found_products = []
        for category, products in self.get_products_by_category().items():
            for product in products.values():
                if min_price <= product["precio"] <= max_price:
                    found_products.append({"Categoria": category, "Producto": product})

        if found_products:
            print("Productos encontrados:")
            for i, product in enumerate(found_products):
                print(
                    f"{i + 1}. {product['Categoria']} - {product['Producto']['nombre']} - {product['Producto']['precio']}"
                )
        else:
            print("No se encontraron productos con ese precio.")


# Main entry point
store = Store()
print("-----Bienvenido a nuestra tienda de tecnología!-----")

while True:
    print("\nMENU PRINCIPAL")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    action = input("Seleccione una opción: ")

    if action == "1":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        user = store.login_user(username, password)

        if user:
            if user.role == "admin":
                while True:
                    store.admin_menu()
                    admin_option = int(input("Seleccione una opción: "))
                    if admin_option == 1:
                        store.view_sales()
                    elif admin_option == 2:
                        store.add_product_to_category()
                    elif admin_option == 3:
                        break
                    else:
                        print("Opción inválida.")
            else:
                while True:
                    store.display_main_menu()
                    user_option = int(input("Seleccione una opción: "))
                    if user_option == 1:
                        store.display_categories()
                        category = int(input("Ingrese una categoría: "))
                        if category > 0 and category <= len(store.get_categories()):
                            selected_category = list(store.get_categories().values())[
                                category - 1
                            ]
                            store.display_products(selected_category)
                            product_index = int(input("Ingrese un producto: "))
                            store.add_product(selected_category, product_index)
                        else:
                            print("Ingrese un número válido.")
                    elif user_option == 2:
                        store.remove_product()
                    elif user_option == 3:
                        store.complete_sale()
                    elif user_option == 4:
                        store.view_cart()
                    elif user_option == 5:
                        store.search_by_brand()
                    elif user_option == 6:
                        store.search_by_price()
                    elif user_option == 7:
                        print("-----Gracias por visitarnos!-----")
                        break
                    else:
                        print("Opción inválida.")

    elif action == "2":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        name = input("Ingrese su nombre: ")
        role = input("Ingrese su rol (admin/user): ").lower()
        if role in ["admin", "user"]:
            store.register_user(username, password, name, role)
        else:
            print("Rol no válido, solo 'admin' o 'user'.")

    elif action == "3":
        print("-----Gracias por visitarnos!-----")
        break

    else:
        print("Opción inválida.")
