# repository/customer_repository.py
from domain.customer import Customer
from utils.database import database


class CustomerRepository:

    def __init__(self) -> None:
        self.database = database["cine"]
        database.create_table("customers", ["name TEXT", "taxpayer_id TEXT PRIMARY KEY"])

    def create_account(self, name: str, taxpayer_id: str) -> None:
        try:
            customer = self.get_account(taxpayer_id, creation=True)
            if customer.get_document() is not None:
                raise ValueError("Cliente já cadastrado!")
            self.database.insert("customers", ("name", "taxpayer_id"), (name, taxpayer_id))
        except Exception as e:
            raise f"Erro ao criar cliente: {e}"

    def update_account(self, taxpayer_id: str, new_name: str) -> str:
        try:
            customer = self.get_account(taxpayer_id)
            old_name = customer.get_name()
            self.database.update("customers", "name", "taxpayer_id", (new_name, taxpayer_id))
            return old_name
        except Exception as e:
            raise f"Erro ao atualizar cliente: {e}"

    def delete_account(self, taxpayer_id: str) -> Customer:
        try:
            customer = self.get_account(taxpayer_id)
            affected_lines = self.database.delete("customers", "taxpayer_id", (taxpayer_id,))[0]
            return customer
        except Exception as e:
            raise f"Erro ao deletar cliente: {e}"

    def get_account(self, taxpayer_id: str, creation: bool = False) -> Customer | None:
        try:
            name, customer_id = self.database.select(
                ["name", "taxpayer_id"], "customers", "taxpayer_id", (taxpayer_id,), "one")[0]
            if not creation and customer_id is None:
                raise ValueError("Cliente inexistente! Por favor, crie uma conta primeiro.")
            elif creation and customer_id is None:
                return None
            return Customer(name, customer_id)
        except Exception as e:
            raise f"Erro ao buscar cliente: {e}"
