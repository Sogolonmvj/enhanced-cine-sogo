# repositories/movie_repository.py
from _pydecimal import Decimal

from domain.movie import Movie


class MovieRepository:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title: str, room_number: int, capacity: int, ticket_price: Decimal()):
        if room_number in self.movies:
            raise ValueError("Sala já ocupada!")
        self.movies[room_number] = Movie(title, room_number, capacity, ticket_price)

    def list_movies(self):
        return list(self.movies.values())

    def get_movie_by_room(self, room_number: int):
        if room_number not in self.movies:
            raise ValueError("Sala inexistente!")
        return self.movies[room_number]

    def book_tickets(self, room_number: int, quantity: int):
        if room_number not in self.movies:
            raise ValueError("Sala inexistente!")
        if quantity <= 0:
            raise ValueError("Quantidade inválida de ingressos!")
        movie = self.get_movie_by_room(room_number)
        movie.book_seats(quantity)

    def has_ticket_sold(self, room_number: int):
        if room_number not in self.movies:
            raise ValueError("Sala inexistente!")
        movie = self.get_movie_by_room(room_number)
        return movie.booked_seats > 0
