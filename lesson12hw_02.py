from datetime import datetime


class Item:
    def __init__(self, name, price, description, dimensions, shelf_life, discount=0):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.shelf_life = shelf_life
        self.discount = discount

    def __str__(self):
        return (
            f"{self.name}, price: {self.price}, description: {self.description}, "
            f"dimensions: {self.dimensions}, term: {self.shelf_life}, "
            f"discount: {self.discount}%"
        )


class User:
    def __init__(self, name, middle_name, surname, phone_number, address):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.name} {self.middle_name} {self.surname}"


class Purchase:
    def __init__(self, user, delivery, delivery_address, delivery_phone, delivery_datetime):
        self.user = user
        self.delivery = delivery
        self.delivery_address = delivery_address
        self.delivery_phone = delivery_phone
        self.delivery_datetime = delivery_datetime
        self.products = {}

    def add_item(self, item, count):
        self.products[item] = count

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())

    def get_discounted_total(self):
        return sum(
            (item.price - item.price * item.discount / 100) * count
            for item, count in self.products.items()
        )

    def __str__(self):
        items_str = "\n".join(
            [f"{item.name}: {count} pcs., {item}" for item, count in self.products.items()]
        )
        total_price = self.get_total()
        discounted_price = self.get_discounted_total()

        return (
            f"User: {self.user}\n"
            f"Phone: {self.user.phone_number}\n"
            f"Address: {self.user.address}\n"
            f"Delivery: {self.delivery}\n"
            f"Delivery Phone: {self.delivery_phone}\n"
            f"Delivery Address: {self.delivery_address}\n"
            f"Delivery Date: {self.delivery_datetime.date()}\n"
            f"Delivery Time: {self.delivery_datetime.time()}\n"
            f"Items:\n{items_str}\n"
            f"Total price: {total_price}\n"
            f"Discounted price: {discounted_price}"
        )


# Тестування
lemon = Item("lemon", 5, "yellow", "small", "7 days", 10)
apple = Item("apple", 2, "red", "middle", "14 days", 5)
banana = Item("banana", 3, "yellow", "large", "5 days", 7)
orange = Item("orange", 4, "orange", "medium", "10 days", 3)

buyer = User(
    "Svyryd",
    "Petrovych",
    "Holokhvastov",
    "123456789",
    "Kyiv, Khreschatyk 1"
)

delivery = User(
    "Ivan",
    "Sydorovych",
    "Sydorenko",
    "987654321",
    "Kyiv, Peremohy 10")

delivery_datetime = datetime(2023, 6, 10, 15, 30)
delivery_address = "Kyiv, Peremohy 10"
delivery_phone = "987654321"

cart = Purchase(buyer, delivery, delivery_address, delivery_phone, delivery_datetime)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
cart.add_item(banana, 5)
cart.add_item(orange, 3)

print(cart)