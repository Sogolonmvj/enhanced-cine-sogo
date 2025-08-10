import pytest
from decimal import Decimal
from domain.movie import Movie
from domain.customer import Customer
from domain.product import Product
from repositories.movie_repository import MovieRepository
from repositories.customer_repository import CustomerRepository
from services.ticket_purchase_service import TicketPurchaseService


@pytest.fixture
def setup():
    movie_repo = MovieRepository()
    customer_repo = CustomerRepository()
    products = [Product("Refrigerante", Decimal('4.00')),
                Product("Pipoca", Decimal('3.00')),
                Product("Doce", Decimal('2.00'))]

    movie_repo.add_movie("Matrix", 1, 10, Decimal('25.00'))
    customer = Customer("Joao", "123")
    customer_repo.create_account(customer.get_name(), customer.get_document())

    service = TicketPurchaseService(movie_repo, customer_repo, products)
    return service, customer_repo, movie_repo


def test_purchase_ticket_success(setup):
    service, _, _ = setup
    result = service.purchase_ticket("123", 1, 2, ["Pipoca", "Refrigerante"])
    assert "Joao" in result['customer']
    assert "Matrix" in result['movie']


def test_purchase_ticket_invalid_customer(setup):
    service, _, _ = setup
    with pytest.raises(ValueError, match="Cliente inexistente!"):
        service.purchase_ticket("999", 1, 1, [])


def test_purchase_ticket_with_unavailable_seats(setup):
    service, _, _ = setup
    service.purchase_ticket("123", 1, 10, [])
    with pytest.raises(ValueError):
        service.purchase_ticket("123", 1, 1, [])


def test_purchase_ticket_with_invalid_room(setup):
    service, _, _ = setup
    with pytest.raises(ValueError):
        service.purchase_ticket("123", 999, 1, [])


# def test_purchase_ticket_with_invalid_product(setup):
#     service, _, _ = setup
#     with pytest.raises(ValueError):
#         service.purchase_ticket("123", 1, 1, ["InvalidProduct"])


def test_purchase_ticket_with_empty_product_list(setup):
    service, _, _ = setup
    result = service.purchase_ticket("123", 1, 1, [])
    assert result['products'] == []
    assert result['total_price'] == Decimal('25.00')  # Only ticket price


# def test_purchase_ticket_with_multiple_products(setup):
#     service, _, _ = setup
#     result = service.purchase_ticket("123", 1, 2, ["Pipoca", "Refrigerante"])
#     assert len(result['products']) == 2
#     assert result['total_price'] == Decimal('25.00') + Decimal('3.00') + Decimal(
#         '4.00')  # Ticket + Pipoca + Refrigerante
