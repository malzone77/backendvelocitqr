from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para criar banco de dados e tabela (se não existir)
def criar_banco():
    conn = sqlite3.connect('vendas_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastro_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf_cnpj TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            numero_peca TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para salvar dados no banco
def salvar_no_banco(data):
    conn = sqlite3.connect('vendas_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cadastro_venda (nome, cpf_cnpj, email, telefone, numero_peca)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['Nome'], data['CpfCnpj'], data['Email'], data['Telefone'], data['NumeroPeca']))

    conn.commit()
    conn.close()

# Rota para cadastrar uma venda
@app.route('/cadastrar_venda', methods=['POST'])
def cadastrar_venda():
    data = request.json
    
    # Verificar se todos os campos necessários estão presentes
    required_fields = ['Nome', 'CpfCnpj', 'Email', 'Telefone', 'NumeroPeca']
    for field in required_fields:
        if field not in data:
            return jsonify({"status": "erro", "mensagem": f"Campo {field} ausente"}), 400

    # Processar e salvar os dados
    salvar_no_banco(data)
    return jsonify({"status": "sucesso", "mensagem": "Venda cadastrada com sucesso"}), 200

@app.route('/')
def home():
    return "Servidor Flask está funcionando!"


if __name__ == "__main__":
    criar_banco()  # Garantir que a tabela exista
    app.run(debug=True)
