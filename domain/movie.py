# domain/movie.py
from _pydecimal import Decimal


class Movie:
    def __init__(self, title: str, room_number: int, ticket_price: Decimal()) -> None:
        self.title = title
        self.room_number = room_number
        self.price = ticket_price

    def get_price(self) -> Decimal():
        return self.price

    def get_room_number(self) -> int:
        return self.room_number

    def get_title(self) -> str:
        return self.title
