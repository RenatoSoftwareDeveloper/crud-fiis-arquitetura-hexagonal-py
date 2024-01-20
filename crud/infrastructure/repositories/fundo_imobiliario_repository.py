
from domain.ports.outbound.fundo_imobiliario_outbound_port import FundoImobiliarioOutboundPort

class FundoImobiliarioRepository(FundoImobiliarioOutboundPort):
    def __init__(self):
        self.fundos = {}

    def salvar_fundo_imobiliario(self, fundo):
        if fundo.id is None:
            fundo.id = len(self.fundos) + 1
        self.fundos[fundo.id] = fundo
        return fundo

    def buscar_fundo_imobiliario_por_id(self, fundo_id):
        return self.fundos.get(fundo_id)

    def listar_fundos_imobiliarios(self):
        return list(self.fundos.values())

    def remover_fundo_imobiliario(self, fundo_id):
        if fundo_id in self.fundos:
            del self.fundos[fundo_id]
