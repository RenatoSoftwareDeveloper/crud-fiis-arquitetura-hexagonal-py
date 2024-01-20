
from domain.models.fundo_imobiliario import FundoImobiliario

class FundoImobiliarioUseCase:
    def __init__(self, outbound_port):
        self.outbound_port = outbound_port

    def listar_fundos_imobiliarios(self):
        return self.outbound_port.listar_fundos_imobiliarios()

    def obter_fundo_imobiliario_por_id(self, fundo_id):
        return self.outbound_port.buscar_fundo_imobiliario_por_id(fundo_id)

    def criar_fundo_imobiliario(self, nome, descricao, valor):
        fundo = FundoImobiliario(id=None, nome=nome, descricao=descricao, valor=valor)
        return self.outbound_port.salvar_fundo_imobiliario(fundo)

    def atualizar_fundo_imobiliario(self, fundo):
        return self.outbound_port.salvar_fundo_imobiliario(fundo)

    def excluir_fundo_imobiliario(self, fundo_id):
        return self.outbound_port.remover_fundo_imobiliario(fundo_id)