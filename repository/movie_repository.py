# repository/movie_repository.py
from _pydecimal import Decimal

from domain.movie import Movie
from util.database import database


class MovieRepository:
    def __init__(self) -> None:
        self.database = database["cine"]
        database.create_table("movies", ["title TEXT", "room_number INTEGER PRIMARY KEY",
                                         "capacity INTEGER", "ticket_price REAL", "booked_seats INTEGER"])

    def add_movie(self, title: str, room_number: int, capacity: int, ticket_price: Decimal()) -> None:
        try:
            movie = self.get_movie_by_room(room_number)
            if movie is not None:
                raise ValueError("Sala já ocupada!")
            self.database.insert("movies",
                                 ("title", "room_number", "capacity", "ticket_price"),
                                 (title, room_number, capacity, Decimal(ticket_price)))
        except Exception as e:
            raise f"Erro ao buscar sala: {e}"

    def list_movies(self) -> list[Movie]:
        try:
            movies = []
            rows = self.database.select(
                ["title", "room_number", "capacity", "ticket_price", "booked_seats"], "movies")
            for row in rows:
                title, room, capacity, price, booked_seats = row
                movie = Movie(title, room, capacity, Decimal(str(price)))
                movies = movies.append(movie)
            return movies
        except Exception as e:
            raise f"Erro ao listar filmes: {e}"

    def get_movie_by_room(self, room_number: int) -> Movie:
        try:
            title, room, capacity, price, booked_seats = self.database.select(
                ["title", "room_number", "capacity", "ticket_price", "booked_seats"],
                "movies", "room_number", (room_number,), "one")[0]
            if room is None:
                raise ValueError("Sala inexistente!")
            movie = Movie(title, room, Decimal(str(price)))
            movie.booked_seats = booked_seats if booked_seats is not None else 0
            return movie
        except Exception as e:
            raise f"Erro ao buscar sala: {e}"

    def book_tickets(self, room_number: int, quantity: int) -> None:
        try:
            if quantity <= 0:
                raise ValueError("Quantidade inválida de ingressos!")
            booked_seats, capacity = self.database.select(
                ["booked_seats", "capacity"], "movies", "room_number", (room_number,), "one")[0]
            if booked_seats is None or booked_seats < 0:
                raise ValueError("Sala inexistente!")
            if booked_seats == capacity:
                raise ValueError("Sala lotada!")
            booked_seats = booked_seats + quantity
            self.database.update(
                "movies", "booked_seats", "room_number", (booked_seats, room_number))
        except Exception as e:
            raise f"Erro ao buscar sala: {e}"

    def has_ticket_sold(self, room_number: int) -> bool:
        try:
            booked_seats = self.database.select(
                ["booked_seats"], "movies", "room_number", (room_number,), "one")[0]
            if booked_seats is None or booked_seats < 0:
                raise ValueError("Sala inexistente!")
            return booked_seats > 0
        except Exception as e:
            raise f"Erro ao buscar sala: {e}"
