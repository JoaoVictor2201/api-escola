# app/routes/turma_routes.py

from flask import Blueprint, request, jsonify
from app.controllers import turma_controller

turma_bp = Blueprint('turma_bp', __name__, url_prefix='/turmas')

@turma_bp.route('/', methods=['GET'])
def get_turmas():
    turmas = turma_controller.get_all_turmas()
    return jsonify(turmas)

@turma_bp.route('/', methods=['POST'])
def create_turma():
    data = request.get_json()
    if not data or not 'descricao' in data or not 'professor_id' in data:
        return jsonify({'error': 'Dados insuficientes'}), 400
    
    nova_turma = turma_controller.create_turma(data)
    if not nova_turma:
        return jsonify({'error': 'Professor não encontrado'}), 404

    return jsonify(nova_turma), 201

@turma_bp.route('/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    turma = turma_controller.get_turma_by_id(turma_id)
    if turma:
        return jsonify(turma)
    return jsonify({'error': 'Turma não encontrada'}), 404

@turma_bp.route('/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    data = request.get_json()
    turma_atualizada = turma_controller.update_turma(turma_id, data)

    if 'error' in turma_atualizada:
        return jsonify(turma_atualizada), 404
    
    return jsonify(turma_atualizada)

@turma_bp.route('/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    sucesso = turma_controller.delete_turma(turma_id)
    if sucesso:
        return jsonify({'message': 'Turma deletada com sucesso'})
    return jsonify({'error': 'Turma não encontrada'}), 404