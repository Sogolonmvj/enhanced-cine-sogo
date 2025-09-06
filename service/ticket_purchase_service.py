# service/ticket_purchase_service.py
from domain.product import Product
from repository.customer_repository import CustomerRepository
from repository.movie_repository import MovieRepository


class TicketPurchaseService:
    def __init__(self,
                 movie_repository: MovieRepository,
                 customer_repository: CustomerRepository,
                 products: [Product]) -> None:
        self.movie_repository = movie_repository
        self.customer_repository = customer_repository
        self.products = products

    def purchase_ticket(self,
                        customer_id: str,
                        room_number: int,
                        quantity: int,
                        selected_product_names: list) -> dict:
        try:
            customer = self.customer_repository.get_account(customer_id)
            if customer.get_document() is None:
                raise ValueError("Cliente inexistente!")
        except Exception as e:
            raise ValueError("Erro ao buscar cliente: " + str(e))

        movie = self.movie_repository.get_movie_by_room(room_number)  ## alterar para consultar banco de dados
        movie.book_seats(quantity)

        selected_products = []
        total_price = quantity * movie.get_price()

        for product_name in selected_product_names:
            for product in self.products:
                if product.name.lower() == product_name.lower():
                    selected_products.append((product.get_name(), product.get_price()))
                    total_price += product.get_price()

        return {
            "customer": self.__get_customer_name_by_id(customer_id),
            "movie": movie.title,
            "room": movie.room_number,
            "tickets": quantity,
            "products": [products[0] for products in selected_products],
            "total_price": total_price
        }

    def __get_customer_name_by_id(self, customer_id: str) -> str:
        try:
            name = self.customer_repository.get_account(customer_id).get_name()
            return name
        except Exception as e:
            raise ValueError("Erro ao buscar cliente: " + str(e))
