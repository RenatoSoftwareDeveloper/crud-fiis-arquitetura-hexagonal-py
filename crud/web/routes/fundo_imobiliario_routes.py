
from flask import Blueprint
from adapters.controller.fundo_imobiliario_controller import FundoImobiliarioController
from domain.use_cases.fundo_imobiliario_use_case import FundoImobiliarioUseCase
from infrastructure.repositories.fundo_imobiliario_repository import FundoImobiliarioRepository

fundo_imobiliario_blueprint = Blueprint('fundo_imobiliario', __name__)
repository = FundoImobiliarioRepository()
use_case = FundoImobiliarioUseCase(repository)
controller = FundoImobiliarioController(use_case)

@fundo_imobiliario_blueprint.route('/fundo_imobiliario', methods=['GET'])
def listar_fundos_imobiliarios():
    return controller.listar_fundos_imobiliarios()

@fundo_imobiliario_blueprint.route('/fundo_imobiliario/<int:fundo_id>', methods=['GET'])
def obter_fundo_imobiliario_por_id(fundo_id):
    return controller.obter_fundo_imobiliario_por_id(fundo_id)

@fundo_imobiliario_blueprint.route('/fundo_imobiliario', methods=['POST'])
def criar_fundo_imobiliario():
    return controller.criar_fundo_imobiliario()

@fundo_imobiliario_blueprint.route('/fundo_imobiliario/<int:fundo_id>', methods=['PUT'])
def atualizar_fundo_imobiliario(fundo_id):
    return controller.atualizar_fundo_imobiliario(fundo_id)

@fundo_imobiliario_blueprint.route('/fundo_imobiliario/<int:fundo_id>', methods=['DELETE'])
def excluir_fundo_imobiliario(fundo_id):
    return controller.excluir_fundo_imobiliario(fundo_id)
