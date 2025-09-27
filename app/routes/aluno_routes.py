# app/routes/aluno_routes.py

from flask import Blueprint, request, jsonify
from app.controllers import aluno_controller

aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET', 'POST'])
def handle_alunos():
    if request.method == 'GET':
        alunos = aluno_controller.get_all_alunos()
        return jsonify(alunos)
    elif request.method == 'POST':
        data = request.get_json()
        if not data or not 'nome' in data or not 'turma_id' in data:
            return jsonify({'error': 'Dados insuficientes'}), 400
        
        novo_aluno = aluno_controller.create_aluno(data)
        if not novo_aluno:
            return jsonify({'error': 'Turma não encontrada'}), 404
        return jsonify(novo_aluno), 201

@aluno_bp.route('/<int:aluno_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_aluno(aluno_id):
    if request.method == 'GET':
        aluno = aluno_controller.get_aluno_by_id(aluno_id)
        if aluno:
            return jsonify(aluno)
        return jsonify({'error': 'Aluno não encontrado'}), 404
    
    elif request.method == 'PUT':
        data = request.get_json()
        aluno_atualizado = aluno_controller.update_aluno(aluno_id, data)
        if 'error' in aluno_atualizado:
            return jsonify(aluno_atualizado), 404
        return jsonify(aluno_atualizado)
    
    elif request.method == 'DELETE':
        sucesso = aluno_controller.delete_aluno(aluno_id)
        if sucesso:
            return jsonify({'message': 'Aluno deletado com sucesso'})
        return jsonify({'error': 'Aluno não encontrado'}), 404