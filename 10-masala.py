import os
os.system("cls")

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Laptop(Product):
    def __init__(self, title, price, cpu_model):
        super().__init__(title, price)
        self.cpu_model = cpu_model

laptops = [
    Laptop("MacBook Pro", 2200, "M2"),
    Laptop("HP Spectre", 1800, "Intel i7"),
    Laptop("Lenovo", 1700, "Intel i5")
]

eng_qimmat = max(laptops, key=lambda laptop: laptop.price)

print(f"{eng_qimmat.title}")
print(f"Narxi: {eng_qimmat.price}")
print(f"cpu_modeli: {eng_qimmat.cpu_model}")