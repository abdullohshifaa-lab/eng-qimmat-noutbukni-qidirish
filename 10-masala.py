import os
os.system("cls")

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Laptop(Product):
    def __init__(self, title, price):
        super().__init__(title, price)

laptops = [
    Laptop("MacBook Pro", 2200),
    Laptop("HP Spectre", 1800),
    Laptop("Lenovo", 1700)
]

eng_qimmat = max(laptops, key=lambda laptop: laptop.price)

print(f"{eng_qimmat.title}")
print(f"Narxi: {eng_qimmat.price}")