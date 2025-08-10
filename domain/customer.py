# domain/customer.py
class Customer:
    def __init__(self, name: str, taxpayer_id: str):
        self.name = name
        self.document = taxpayer_id

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_document(self):
        return self.document
