# domain/product.py
from _pydecimal import Decimal


class Product:
    def __init__(self, name: str, price: Decimal()):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
