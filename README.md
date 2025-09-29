# API de Gestão Escolar em Flask

Este projeto consiste em uma API RESTful completa construída com Flask para o gerenciamento de Professores, Turmas e Alunos de uma instituição de ensino.

## Arquitetura Utilizada

A aplicação foi desenvolvida seguindo uma arquitetura baseada no padrão **MVC (Model-View-Controller)**, com foco no backend (sem a camada de View). A estrutura é organizada da seguinte forma:

-   **Models**: Representam a estrutura das tabelas do banco de dados (Professor, Turma, Aluno) utilizando o ORM SQLAlchemy. 
-   **Controllers**: Contêm toda a lógica de negócio para manipular os dados (operações CRUD).
-   **Routes (Blueprints)**: Definem os endpoints da API, recebem as requisições HTTP e as direcionam para as funções apropriadas nos controllers.

## Funcionalidades

-   **CRUD Completo**: Implementação dos métodos GET, POST, PUT e DELETE para as três entidades principais: Professores, Turmas e Alunos. 
-   **Relacionamentos**: Mapeamento dos relacionamentos One-to-Many entre Professor-Turma e Turma-Aluno.
-   **Persistência de Dados**: Utilização de um banco de dados SQLite com o ORM SQLAlchemy para persistência. 
-   **Documentação Interativa**: Documentação completa da API gerada automaticamente com Swagger (Flasgger), permitindo a visualização e teste dos endpoints diretamente pelo navegador. 

## Tecnologias Utilizadas

-   **Python 3**
-   **Flask**: Micro-framework web para a construção da API.
-   **Flask-SQLAlchemy**: Integração do SQLAlchemy para manipulação do banco de dados.
-   **Flasgger**: Geração de documentação Swagger UI.

## Como Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

**1. Clonar o Repositório**
```bash
git clone https://github.com/JoaoVictor2201/api-escola
cd api-escola
```

**2. Criar e Ativar o Ambiente Virtual**
```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
```

**3. Instalar as Dependências**
```bash
pip install -r requirements.txt
```

**4. Criar o Banco de Dados**
Execute o terminal interativo do Flask e crie as tabelas.
```bash
flask shell
```
Dentro do shell, execute:
```python
from app import db, create_app
app = create_app()
with app.app_context():
    db.create_all()
exit()
```

**5. Iniciar a Aplicação**
```bash
python run.py
```

A API estará rodando em `http://127.0.0.1:5000`.

## Endpoints da API

A documentação completa e interativa dos endpoints está disponível em:

-   **Swagger UI**: [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)
