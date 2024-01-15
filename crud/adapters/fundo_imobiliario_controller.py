# adapters/controllers.py
from flask import Flask, jsonify, request
from application.fundo_imobiliario_service import FundoImobiliarioService


app = Flask(__name__)
fundo_service = FundoImobiliarioService()

@app.route('/fundos', methods=['GET'])
def get_all():
    fundos = fundo_service.get_all()
    return jsonify([f.__dict__ for f in fundos]), 200

@app.route('/fundos/<int:fundo_id>', methods=['GET'])
def get_by_id(fundo_id):
    fundo = fundo_service.get_by_id(fundo_id)
    if fundo:
        return jsonify(fundo.__dict__), 200
    return jsonify({'error': 'Fundo não encontrado'}), 404

@app.route('/fundos', methods=['POST'])
def create():
    data = request.get_json()
    nome = data.get('nome')
    ticker = data.get('ticker')
    if nome and ticker:
        fundo = fundo_service.create(nome, ticker)
        return jsonify(fundo.__dict__), 201
    return jsonify({'error': 'Nome e ticker são obrigatórios'}), 400

@app.route('/fundos/<int:fundo_id>', methods=['PUT'])
def update(fundo_id):
    data = request.get_json()
    nome = data.get('nome')
    ticker = data.get('ticker')
    fundo = fundo_service.update(fundo_id, nome, ticker)
    if fundo:
        return jsonify(fundo.__dict__), 200
    return jsonify({'error': 'Fundo não encontrado'}), 404

@app.route('/fundos/<int:fundo_id>', methods=['DELETE'])
def delete(fundo_id):
    success, message = fundo_service.delete(fundo_id)
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 404

if __name__ == '__main__':
    app.run(debug=True)
