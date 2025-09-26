from flask import Blueprint, request, jsonify
from app.controllers import professor_controller

professor_bp = Blueprint('professor_bp', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def get_professores():
    professores = professor_controller.get_all_professores()
    return jsonify(professores)

@professor_bp.route('/', methods=['POST'])
def create_professor():
    data = request.get_json()
    if not data or not 'nome' in data:
        return jsonify({'error': 'Dados insuficientes'}), 400
    
    novo_professor = professor_controller.create_professor(data)
    return jsonify(novo_professor), 201

@professor_bp.route('/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    professor = professor_controller.get_professor_by_id(professor_id)
    if professor:
        return jsonify(professor)
    return jsonify({'error': 'Professor não encontrado'}), 404

@professor_bp.route('/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.get_json()
    professor_atualizado = professor_controller.update_professor(professor_id, data)
    if professor_atualizado:
        return jsonify(professor_atualizado)
    return jsonify({'error': 'Professor não encontrado'})

@professor_bp.route('/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    deletado = professor_controller.delete_professor(professor_id)
    if deletado:
        return jsonify({'message': 'Professor deletado com sucesso'})
    return jsonify({'error': 'Professor não encontrado'})