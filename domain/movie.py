# domain/movie.py
from _pydecimal import Decimal


class Movie:
    def __init__(self, title: str, room_number: int, capacity: int, ticket_price: Decimal()):
        self.title = title
        self.room_number = room_number
        self.capacity = capacity
        self.price = ticket_price
        self.booked_seats = 0

    def book_seats(self, quantity):
        if quantity > self.available_seats():
            raise ValueError("Quantidade insuficiente de vagas disponíveis!")
        self.booked_seats += quantity

    def available_seats(self):
        return self.capacity - self.booked_seats

    def get_price(self):
        return self.price

    def get_capacity(self):
        return self.capacity

    def get_booked_seats(self):
        return self.booked_seats

    def get_room_number(self):
        return self.room_number

    def get_title(self):
        return self.title
