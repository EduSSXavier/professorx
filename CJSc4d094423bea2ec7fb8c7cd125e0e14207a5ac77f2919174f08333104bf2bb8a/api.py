from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # Permite requisições de outros domínios

# Dados de exemplo (banco de dados simulado)
livros = [
    {"id": 1, "titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"id": 2, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 3, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937},
    {"id": 4, "titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967},
]

# Rotas 
@app.route('/')
def home():
    return jsonify({
        "mensagem": "Bem-vindo à API de Livros!",
        "rotas": {
            "/livros": "Lista todos os livros",
            "/livros/<id>": "Busca um livro por ID"
            }
        })

# GET - Listar todos os livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

# GET - Buscar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = next((l for l in livros if l['id'] == id), None)
    if livro:
        return jsonify(livro)
    else:
        return jsonify({"erro": "Livro não encontrado"}), 404

# Iniciar o servidor
print("API rodando na porta 5000")
app.run(port=5000)