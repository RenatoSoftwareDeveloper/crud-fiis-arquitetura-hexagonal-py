# crud/adapters/validations/fundo_imobiliario_validator.py

class FundoImobiliarioValidator:
    @staticmethod
    def validate_nome(nome):
        if not nome:
            return False, "O nome do fundo imobiliário é obrigatório"
        return True, None

    @staticmethod
    def validate_descricao(descricao):
        if not descricao:
            return False, "A descrição do fundo imobiliário é obrigatória"
        return True, None

    @staticmethod
    def validate_valor(valor):
        if valor is None:
            return False, "O valor do fundo imobiliário é obrigatório"
        if not isinstance(valor, (int, float)):
            return False, "O valor do fundo imobiliário deve ser numérico"
        return True, None

    @staticmethod
    def validate_listagem():
        # Adicione suas regras de validação para listar fundos imobiliários, se necessário
        return True, None

    @staticmethod
    def validate_fundo_id(fundo_id):
        if not fundo_id or not str(fundo_id).isdigit():
            return False, "O ID do fundo imobiliário é inválido"
        return True, None
    
    @staticmethod
    def validate_existencia_fundo(fundo):
        if not fundo:
            return False, "Fundo imobiliário não encontrado"
        return True, None
    
    @staticmethod
    def validate_exclusao_fundo(fundo):
        # Adicione aqui regras específicas para validar a exclusão, se necessário
        # Neste exemplo, não temos regras específicas para validar a exclusão com sucesso
        return True, "Fundo imobiliário excluído com sucesso"
    
    @staticmethod
    def mensagem_exclusao(fundo):
        return True, f"Fundo imobiliário ID {fundo} excluído com sucesso"