# infrastructure/repositories.py
class FundoImobiliarioRepository:
    def __init__(self):
        self.fundos = []

    def get_all(self):
        return self.fundos

    def get_by_id(self, fundo_id):
        return next((f for f in self.fundos if f.id == fundo_id), None)

    def create(self, fundo):
        fundo.id = len(self.fundos) + 1
        self.fundos.append(fundo)
        return fundo

    def update(self, fundo):
        existing_fundo = self.get_by_id(fundo.id)
        if existing_fundo:
            existing_fundo.nome = fundo.nome
            existing_fundo.ticker = fundo.ticker
            return existing_fundo
        return None

    def delete(self, fundo_id):
        existing_fundo = self.get_by_id(fundo_id)
        if existing_fundo:
            self.fundos.remove(existing_fundo)
            return True, "Fundo imobiliário excluído com sucesso!"
        return False, "Fundo não encontrado"
