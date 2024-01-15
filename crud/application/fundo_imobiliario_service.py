# application/services.py
from domain.fundo_imobiliario import FundoImobiliario
from infrastructure.fundo_imobiliario_repositories import FundoImobiliarioRepository

class FundoImobiliarioService:
    def __init__(self):
        self.repository = FundoImobiliarioRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, fundo_id):
        return self.repository.get_by_id(fundo_id)

    def create(self, nome, ticker):
        fundo = FundoImobiliario(None, nome, ticker)
        return self.repository.create(fundo)

    def update(self, fundo_id, nome, ticker):
        fundo = FundoImobiliario(fundo_id, nome, ticker)
        return self.repository.update(fundo)

    def delete(self, fundo_id):
        return self.repository.delete(fundo_id)
