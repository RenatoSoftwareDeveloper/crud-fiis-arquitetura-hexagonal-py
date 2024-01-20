from flask import jsonify, request
from domain.validations.fundo_imobiliario_validator import FundoImobiliarioValidator
from domain.use_cases.fundo_imobiliario_use_case import FundoImobiliarioUseCase


class FundoImobiliarioController:
    def __init__(self, use_case: FundoImobiliarioUseCase):
        self.use_case = use_case

    def listar_fundos_imobiliarios(self):
        fundos = self.use_case.listar_fundos_imobiliarios()
        return jsonify([f.__dict__ for f in fundos])

    def obter_fundo_imobiliario_por_id(self, fundo_id):
        # Validação do método obter_fundo_imobiliario_por_id
        is_valid_fundo_id, fundo_id_error = FundoImobiliarioValidator.validate_fundo_id(fundo_id)
        if not is_valid_fundo_id:
            return jsonify({"message": fundo_id_error}), 400

        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)
        if fundo:
            return jsonify(fundo.__dict__)
        return jsonify({"message": "Fundo imobiliário não encontrado"}), 404

    def criar_fundo_imobiliario(self):
        data = request.get_json()
        nome = data.get('nome')
        descricao = data.get('descricao')
        valor = data.get('valor')

        # Validação dos campos usando a camada de validação
        is_valid_nome, nome_error = FundoImobiliarioValidator.validate_nome(nome)
        is_valid_descricao, descricao_error = FundoImobiliarioValidator.validate_descricao(descricao)
        is_valid_valor, valor_error = FundoImobiliarioValidator.validate_valor(valor)

        if not is_valid_nome:
            return jsonify({"message": nome_error}), 400
        if not is_valid_descricao:
            return jsonify({"message": descricao_error}), 400
        if not is_valid_valor:
            return jsonify({"message": valor_error}), 400

        novo_fundo = self.use_case.criar_fundo_imobiliario(nome, descricao, valor)
        return jsonify(novo_fundo.__dict__), 201

    def atualizar_fundo_imobiliario(self, fundo_id):
        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)
        if not fundo:
            return jsonify({"message": "Fundo imobiliário não encontrado"}), 404

        data = request.get_json()
        nome = data.get('nome', fundo.nome)
        descricao = data.get('descricao', fundo.descricao)
        valor = data.get('valor', fundo.valor)

        # Validação dos campos usando a camada de validação
        is_valid_nome, nome_error = FundoImobiliarioValidator.validate_nome(nome)
        is_valid_descricao, descricao_error = FundoImobiliarioValidator.validate_descricao(descricao)
        is_valid_valor, valor_error = FundoImobiliarioValidator.validate_valor(valor)

        if not is_valid_nome:
            return jsonify({"message": nome_error}), 400
        if not is_valid_descricao:
            return jsonify({"message": descricao_error}), 400
        if not is_valid_valor:
            return jsonify({"message": valor_error}), 400

        fundo.nome = nome
        fundo.descricao = descricao
        fundo.valor = valor

        fundo_atualizado = self.use_case.atualizar_fundo_imobiliario(fundo)
        return jsonify(fundo_atualizado.__dict__)

    def excluir_fundo_imobiliario(self, fundo_id):
        # Validação do método excluir_fundo_imobiliario
        is_valid_fundo_id, fundo_id_error = FundoImobiliarioValidator.validate_fundo_id(fundo_id)
        if not is_valid_fundo_id:
            return jsonify({"message": fundo_id_error}), 400

        fundo = self.use_case.obter_fundo_imobiliario_por_id(fundo_id)

        # Validação de existência do fundo imobiliário
        is_valid_existencia_fundo, existencia_fundo_error = FundoImobiliarioValidator.validate_existencia_fundo(fundo)
        if not is_valid_existencia_fundo:
            return jsonify({"message": existencia_fundo_error}), 404

        # Validação específica para exclusão
        is_valid_exclusao, exclusao_message = FundoImobiliarioValidator.validate_exclusao_fundo(fundo)
        if not is_valid_exclusao:
            return jsonify({"message": exclusao_message}), 400

        self.use_case.excluir_fundo_imobiliario(fundo_id)
        return jsonify({"message": exclusao_message}), 204