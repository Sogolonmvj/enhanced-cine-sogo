# repository/customer_repository.py
from domain.customer import Customer
from util.database import SQLiteDatabase as database


class CustomerRepository:

    def __init__(self) -> None:
        customer_database = database("cine")
        customer_database.create_table(
            table_name="customers",
            column_names=["name TEXT", "taxpayer_id TEXT PRIMARY KEY"]
        )
        self.database = customer_database

    def create_account(self, name: str, taxpayer_id: str) -> None:
        try:
            customer = self.get_account(taxpayer_id, creation=True)
            if customer.get_document() is not None:
                raise ValueError("Cliente já cadastrado!")
            self.database.insert(
                table_name="customers",
                column_names=["name", "taxpayer_id"],
                values=(name, taxpayer_id)
            )
        except Exception as e:
            raise f"Erro ao criar cliente: {e}"

    def update_account(self, taxpayer_id: str, new_name: str) -> str:
        try:
            customer = self.get_account(taxpayer_id)
            old_name = customer.get_name()
            self.database.update(
                table_name="customers",
                column_names=["name"],
                column_name="taxpayer_id",
                values=(new_name, taxpayer_id)
            )
            return old_name
        except Exception as e:
            raise f"Erro ao atualizar cliente: {e}"

    def delete_account(self, taxpayer_id: str) -> Customer:
        try:
            customer = self.get_account(taxpayer_id)
            affected_lines = self.database.delete(
                table_name="customers",
                column_name="taxpayer_id",
                value=(taxpayer_id,)
            )[0]
            return customer
        except Exception as e:
            raise f"Erro ao deletar cliente: {e}"

    def get_account(self, taxpayer_id: str, creation: bool = False) -> Customer | None:
        try:
            name, customer_id = self.database.select(
                column_names=["name", "taxpayer_id"],
                table_name="customers",
                column_name="taxpayer_id",
                value=(taxpayer_id,),
                fetch="one"
            )[0]
            if not creation and customer_id is None:
                raise ValueError("Cliente inexistente! Por favor, crie uma conta primeiro.")
            elif creation and customer_id is None:
                return None
            return Customer(name, customer_id)
        except Exception as e:
            raise f"Erro ao buscar cliente: {e}"

    def has_any_account(self) -> bool:
        try:
            count = self.database.count(
                table_name="customers"
            )
            return count > 0
        except Exception as e:
            raise f"Erro ao verificar clientes: {e}"
