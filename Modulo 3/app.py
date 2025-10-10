from flask import Flask, request, json, jsonify, render_template, redirect, url_for
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario, login_de_usuario, matricular_aluno
from tabelas import Nota, Usuario
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        resultado = ler_dados()
        return render_template('index.html',data=resultado)
    elif request.method == 'POST':
        data = request.get_data()
        usuario_e_nota = json.loads(data)

        user = Usuario(
                        nome=usuario_e_nota["usuario"],
                        email=usuario_e_nota["email"],
                        senha_hash=usuario_e_nota["senha"])
        note = Nota(
                        titulo=usuario_e_nota["titulo"],
                        conteudo=usuario_e_nota["nota"])
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"message": "Usuário e nota criados com sucesso!"}), 201
    else:
        return jsonify({'error': 'Pagina não encontrada!'}), 404

@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_data()
        usuario = json.loads(data)
        user = Usuario(email=usuario["email"], senha_hash=usuario["senha_hash"])
        
        try:
            usr = login_de_usuario(user)
            app.logger.info("Usuário de email: %s logado!" % usuario["email"])
            return redirect(url_for("home", data=usr))
        except Exception as e:
            app.logger.error("Erro de servidor: ", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        return render_template('login.html')
    
@app.route("/remover/usuarios/<id>", methods=['GET', 'DELETE'])
def remover_usuarios(id_usuario):
    if request.method == "DELETE":
        data = request.get_data()
        id_usuario = json.loads(data)
        try:
            deletar_usuario(id_usuario=id_usuario)
            app.logger.info("Usuario do id: %d foi removido com sucesso!" % id_usuario)
            return redirect(url_for("index"))
        except Exception as e:
            app.logger.error("Erro na remoção de usuário: ", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        return render_template('remover.html')

@app.route("/matricula/<id_usuario>/<id_curso>", methods=['GET','POST'])
def matricula(id_usuario, id_curso):
    if request.method == 'POST':
        data = request.get_data()
        ids = json.loads(data)
        try:
            matricular_aluno(id_aluno=id_usuario, id_curso=id_curso)
            app.logger.info("Usuario dov id: %d foi matriculado!" % ids['id_usuario'])
            return redirect(url_for('home'))
        except Exception as e:
            app.logger.error("Erro na matricula de usuario: ", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        return render_template('cursos.html')


if __name__ == "__main__":
    app.run()