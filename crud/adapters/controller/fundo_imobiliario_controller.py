# crud/adapters/controller/fundo_imobiliario_controller.py
from flask import jsonify, request
from domain.use_cases.fundo_imobiliario_use_case import FundoImobiliarioUseCase

class FundoImobiliarioController:
    def __init__(self, use_case: FundoImobiliarioUseCase):
        self.use_case = use_case

    def listar_fundos_imobiliarios(self):
        fundos = self.use_case.listar_fundos_imobiliarios()
        return jsonify([f.__dict__ for f in fundos])

    def obter_fundo_imobiliario_por_id(self, fundo_id):
        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)
        if fundo:
            return jsonify(fundo.__dict__)
        return jsonify({"message": "Fundo imobiliário não encontrado"}), 404

    def criar_fundo_imobiliario(self):
        data = request.get_json()
        nome = data.get('nome')
        descricao = data.get('descricao')
        novo_fundo = self.use_case.criar_fundo_imobiliario(nome, descricao)
        return jsonify(novo_fundo.__dict__), 201

    def atualizar_fundo_imobiliario(self, fundo_id):
        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)
        if not fundo:
            return jsonify({"message": "Fundo imobiliário não encontrado"}), 404

        data = request.get_json()
        fundo.nome = data.get('nome', fundo.nome)
        fundo.descricao = data.get('descricao', fundo.descricao)

        fundo_atualizado = self.use_case.atualizar_fundo_imobiliario(fundo)
        return jsonify(fundo_atualizado.__dict__)

    def excluir_fundo_imobiliario(self, fundo_id):
        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)
        if not fundo:
            return jsonify({"message": "Fundo imobiliário não encontrado"}), 404

        self.use_case.excluir_fundo_imobiliario(fundo_id)
        return jsonify({"message": "Fundo imobiliário excluído"}), 204
