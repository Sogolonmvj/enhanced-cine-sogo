from _decimal import Decimal

from domain.movie import Movie


def test_create_movie():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_title() == 'Matrix'
    assert movie.get_price() == Decimal('20.0')
    assert movie.get_capacity() == 20


def test_book_seats():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    movie.book_seats(5)
    assert movie.get_booked_seats() == 5
    assert movie.available_seats() == 15


def test_book_seats_exceed_capacity():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    movie.book_seats(20)
    try:
        movie.book_seats(5)
    except ValueError as e:
        assert str(e) == "Quantidade insuficiente de vagas disponíveis!"
    else:
        assert False, "Expected ValueError not raised"


def test_available_seats():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.available_seats() == 20
    movie.book_seats(5)
    assert movie.available_seats() == 15
    movie.book_seats(15)
    assert movie.available_seats() == 0


def test_get_room_number():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_room_number() == 1


def test_get_title():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_title() == 'Matrix'


def test_get_price():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_price() == Decimal('20.0')


def test_get_capacity():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_capacity() == 20


def test_get_booked_seats():
    movie = Movie('Matrix', 1, 20, Decimal('20.0'))
    assert movie.get_booked_seats() == 0
    movie.book_seats(5)
    assert movie.get_booked_seats() == 5
    movie.book_seats(10)
    assert movie.get_booked_seats() == 15


# def test_book_seats_negative_quantity():
#     movie = Movie('Matrix', 1, 20, Decimal('20.0'))
#     try:
#         movie.book_seats(-5)
#     except ValueError as e:
#         assert str(e) == "Quantidade insuficiente de vagas disponíveis!"
#     else:
#         assert False, "Expected ValueError not raised"
