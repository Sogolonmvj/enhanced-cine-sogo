# domain/product.py
from _pydecimal import Decimal


class Product:
    def __init__(self, name: str, price: Decimal()) -> None:
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> Decimal():
        return self.price
