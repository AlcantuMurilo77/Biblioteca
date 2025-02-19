
import services
import services.book_services
import services.user_services
import db
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Configuração de CORS global
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})



@app.route("/listarlivros", methods=['GET']) 
def listar_livros():
    livros = db.consultar_livros()
    return jsonify(livros)

@app.route("/cadastrarlivro", methods=['POST']) 
def cadastrar():
    services.book_services.cadastra_livro()
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"})

@app.route("/listarusuarios", methods=['GET']) 
def lista_usuarios():
    usuarios = db.consultar_clientes()
    return jsonify(usuarios)

@app.route("/cadastrarusuario", methods=['POST']) 
def cadastra():
    return services.user_services.cadastrar_usuario()

@app.route("/exibirlivrosemprestadosporusuario", methods=['POST'])
def listar_emprestados():
    return services.book_services.lista_livros_emprestados_usuario()

@app.route("/emprestarlivro", methods=["POST"])
def empresta():
    return services.book_services.emprestar_livro_para_usuario()

@app.route("/devolverlivro", methods=['POST']) 
def devolver():
    return services.book_services.devolver_livro_emprestado()

@app.route("/buscarlivro", methods=['POST']) 
def busca():
    return services.book_services.buscar_livro()

@app.route("/deletalivro", methods=["DELETE"]) 
def deleta():
    return services.book_services.deleta_livro()

if __name__ == '__main__':
    app.run()
