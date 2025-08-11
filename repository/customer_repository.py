# repository/customer_repository.py
from domain.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers = {}

    def create_account(self, name: str, taxpayer_id: str):
        if taxpayer_id in self.customers:
            raise ValueError("Cliente já cadastrado!")
        self.customers[taxpayer_id] = Customer(name, taxpayer_id)

    def update_account(self, taxpayer_id: str, new_name: str):
        if taxpayer_id not in self.customers:
            raise ValueError("Esse cliente não tem uma conta ativa!")
        customer = self.get_account(taxpayer_id)
        old_name = customer.get_name()
        customer.set_name(new_name)
        self.customers[taxpayer_id] = customer
        return old_name

    def delete_account(self, taxpayer_id: str):
        if taxpayer_id not in self.customers:
            raise ValueError("Esse cliente não tem uma conta ativa!")
        customer = self.get_account(taxpayer_id)
        del self.customers[taxpayer_id]
        return customer

    def get_account(self, taxpayer_id: str):
        if taxpayer_id not in self.customers:
            raise ValueError("Cliente inexistente! Por favor, crie uma conta primeiro.")
        return self.customers.get(taxpayer_id)
