from flask import Flask, request, jsonify

app = Flask(__name__)

# Credenciais predefinidas
USUARIO_PRE_DEFINIDO = "velocitqr@gmail.com"
SENHA_PRE_DEFINIDA = "katiau123"

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    # Verificação das credenciais
    if email == USUARIO_PRE_DEFINIDO and senha == SENHA_PRE_DEFINIDA:
        return jsonify({"status": "sucesso", "mensagem": "Login realizado com sucesso"}), 200
    else:
        return jsonify({"status": "erro", "mensagem": "Email ou senha incorretos"}), 401

if __name__ == '__main__':
    app.run(debug=True)
