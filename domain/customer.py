# domain/customer.py
class Customer:
    def __init__(self, name: str, taxpayer_id: str) -> None:
        self.name = name
        self.document = taxpayer_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_document(self) -> str:
        return self.document
