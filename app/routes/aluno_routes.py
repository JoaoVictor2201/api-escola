# app/routes/aluno_routes.py

from flask import Blueprint, request, jsonify
from app.controllers import aluno_controller

aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET', 'POST'])
def handle_alunos():
    """
    Recurso para listar e criar alunos
    ---
    tags:
      - Alunos
    get:
      summary: Lista todos os alunos
      responses:
        200:
          description: Uma lista de alunos
          schema:
            type: array
            items:
              $ref: '#/definitions/Aluno'
    tags:
      - Alunos
    post:
      summary: Cria um novo aluno
      parameters:
        - in: body
          name: body
          schema:
            id: Aluno
            required:
              - nome
              - turma_id
            properties:
              nome:
                type: string
              idade:
                type: integer
              data_nascimento:
                type: string
                format: date
                example: "2005-04-10"
              nota_primeiro_semestre:
                type: number
                format: float
              nota_segundo_semestre:
                type: number
                format: float
              turma_id:
                type: integer
      responses:
        201:
          description: Aluno criado com sucesso
        400:
          description: Dados insuficientes
        404:
          description: Turma não encontrada
    """
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
    """
    Recurso para buscar, atualizar e deletar um aluno específico
    ---
    tags:
      - Alunos
    get:
      summary: Busca um aluno por ID
      parameters:
        - name: aluno_id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Detalhes do aluno
        404:
          description: Aluno não encontrado
    tags:
      - Alunos
    put:
      summary: Atualiza um aluno existente
      parameters:
        - name: aluno_id
          in: path
          type: integer
          required: true
        - in: body
          name: body
          schema:
            $ref: '#/definitions/Aluno'
      responses:
        200:
          description: Aluno atualizado com sucesso
        404:
          description: Aluno ou Turma não encontrado(a)
    tags:
      - Alunos
    delete:
      summary: Deleta um aluno
      parameters:
        - name: aluno_id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Aluno deletado com sucesso
        404:
          description: Aluno não encontrado
    """
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