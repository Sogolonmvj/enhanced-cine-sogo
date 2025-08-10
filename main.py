# main.py
import logging
from _pydecimal import Decimal

from repositories.customer_repository import CustomerRepository
from repositories.movie_repository import MovieRepository
from services.ticket_purchase_service import TicketPurchaseService
from domain.product import Product
from utils.ticket_writer import TicketWriter
from utils.logger import setup_logger


def main():
    setup_logger()
    logger = logging.getLogger(__name__)

    customer_repo = CustomerRepository()
    movie_repo = MovieRepository()
    products = [Product("Refrigerante", Decimal('4.00')),
                Product("Pipoca", Decimal('3.00')),
                Product("Doce", Decimal('2.00'))]
    ticket_service = TicketPurchaseService(movie_repo, customer_repo, products)
    ticket_writer = TicketWriter()

    movie_repo.add_movie("Titanic", 1, 20, Decimal('30.00'))
    movie_repo.add_movie("Pantera Negra", 2, 40, Decimal('50.00'))
    movie_repo.add_movie("Velozes e Furiosos", 3, 20, Decimal('20.00'))
    movie_repo.add_movie("Lobo de Wall Street", 4, 40, Decimal('50.00'))

    while True:
        print("\n--- Cine Sogo ---")
        print("CC. Criar conta")
        if len(customer_repo.customers.values()) > 0:
            print("AC. Alterar conta")
            print("DC. Deletar conta")
        print("MF. Mostrar filmes disponíveis")
        print("RE. Reservar entrada")
        print("CE. Comprar entrada")
        print("SA. Sair")

        choice = input("Escolha uma opção: ")

        try:
            if choice.upper() == "CC":
                taxpayer_id = input("Digite o seu CPF: ")
                name = input("Digite o seu nome: ")
                customer_repo.create_account(name, taxpayer_id)
                logger.info(f"Conta criada: {name}")
                print("Conta criada com sucesso.")
            elif choice.upper() == "AC":
                taxpayer_id = input("Digite o seu CPF: ")
                new_name = input("Digite o novo nome: ")
                old_name = customer_repo.update_account(taxpayer_id, new_name)
                logger.info(f"Nome da conta alterado de {old_name} para {new_name}")
                print("Atualização da conta concluída com sucesso.")
            elif choice.upper() == "DC":
                taxpayer_id = input("Digite o CPF da conta a ser deletada: ")
                customer = customer_repo.delete_account(taxpayer_id)
                logger.info(f"Conta deletada: {customer.get_name()}")
                print("Conta deletada com sucesso.")
            elif choice.upper() == "MF":
                movies = movie_repo.list_movies()
                print("\nFilmes disponíveis:")
                for movie in movies:
                    print(f"Sala {movie.get_room_number()}: {movie.get_title()} ({movie.available_seats()} vagas disponíveis) "
                          f" - Preço: R${movie.get_price():.2f} (unidade)")
            elif choice.upper() == "RE":
                taxpayer_id = input("Digite o seu CPF: ")
                customer = customer_repo.get_account(taxpayer_id)
                room_number = int(input("Digite o número da sala: "))
                quantity = int(input("Digite a quantidade de entrada a ser reservada: "))
                movie_repo.book_tickets(room_number, quantity)
                logger.info(f"{customer.get_name()} reservou {quantity} entradas para a sala {room_number}")
                print("Entradas reservadas com sucesso.")
            elif choice.upper() == "CE":
                taxpayer_id = input("Digite o seu CPF: ")
                customer = customer_repo.get_account(taxpayer_id)
                # Only show booked movies
                booked_movies = [movie for movie in movie_repo.list_movies() if movie.get_booked_seats() > 0]
                if not booked_movies:
                    raise ValueError("Nenhum filme reservado. Por favor, reserve um filme primeiro.")
                print("\nFilmes disponíveis para compra:")
                for movie in booked_movies:
                    print(f"Sala {movie.get_room_number()}: {movie.get_title()} ({movie.get_booked_seats()} vagas "
                          f"reservadas)"
                          f" - Preço: R${movie.get_price():.2f} (unidade)")
                room_number = int(input("Digite o número da sala: "))
                if room_number not in [movie.get_room_number() for movie in booked_movies]:
                    raise ValueError("Sala inexistente ou sem reservas.")
                quantity = int(input("Digite a quantidade de entradas: "))
                for movie in booked_movies:
                    if movie.get_room_number() == room_number:
                        if quantity > movie.get_booked_seats():
                            raise ValueError("A quantidade informada para compra é maior que a quantidade reservada!")
                        break
                need_products = input("Gostaria de solicitar algum produto? (Sim/Não): ")
                selected = []
                if need_products.lower() in ["sim", "s"]:
                    print("Produtos disponíveis:")
                    for product in products:
                        print(f"{product.get_name()} - R${product.get_price():.2f}")
                    selected = input("Digite os produtos selecionados separando com vírgulas: ").replace(".", ",").split(",")
                    selected = [s.strip().capitalize() for s in selected if s.strip()]
                result = ticket_service.purchase_ticket(customer.get_document(), room_number, quantity, selected)
                ticket_writer.write_to_file(customer.get_name(), result)
                logger.info(f"{customer.get_name()} comprou {quantity} entradas na sala {room_number} e os seguintes "
                            f"produtos {selected}")
                print(f"\nCompra finalizada!\nEntradas: {result['tickets']}\nProdutos: {', '.join(result['products'])}\nTotal: R${result['total_price']:.2f}")
                print("Entradas foram geradas em um arquivo.")
            elif choice.upper() == "SA":
                print("Saindo da aplicação.")
                break
            else:
                print("Opção inválida.")
        except ValueError as e:
            logger.error(f"Erro: {e}")
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
