# utils/ticket_writer.py
import os
from datetime import datetime


class TicketWriter:
    def __init__(self, directory: str = "tickets"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def write_to_file(self, customer_name: str, ticket_info: dict):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.directory}/ticket_{customer_name}_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write("--- BILHETE ---\n")
            file.write(f"Cliente: {customer_name}\n")
            file.write(f"Filme: {ticket_info['movie']}\n")
            file.write(f"Sala: {ticket_info['room']}\n")
            file.write(f"Quantidade de entradas: {ticket_info['tickets']}\n")
            file.write("Produtos selecionados:\n")
            for product in ticket_info['products']:
                file.write(f" - {product}\n")
            file.write(f"Valor total: R${ticket_info['total_price']:.2f}\n")
        return filename
