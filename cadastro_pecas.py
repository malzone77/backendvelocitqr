from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para criar banco de dados e tabela (se não existir)
def criar_banco():
    conn = sqlite3.connect('pecas_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastro_peca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo_peca TEXT NOT NULL,
            marca_peca TEXT NOT NULL,
            numero_peca TEXT NOT NULL,
            numero_lote TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para salvar dados no banco
def salvar_no_banco(data):
    conn = sqlite3.connect('pecas_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cadastro_peca (modelo_peca, marca_peca, numero_peca, numero_lote)
        VALUES (?, ?, ?, ?)
    ''', (data['ModeloPeca'], data['MarcaPeca'], data['NumeroPeca'], data['NumeroLote']))

    conn.commit()
    conn.close()

# Rota para cadastrar uma peça
@app.route('/cadastrar_peca', methods=['POST'])
def cadastrar_peca():
    data = request.json
    
    # Verificar se todos os campos necessários estão presentes
    required_fields = ['ModeloPeca', 'MarcaPeca', 'NumeroPeca', 'NumeroLote']
    for field in required_fields:
        if field not in data:
            return jsonify({"status": "erro", "mensagem": f"Campo {field} ausente"}), 400

    # Processar e salvar os dados
    salvar_no_banco(data)
    return jsonify({"status": "sucesso", "mensagem": "Cadastro realizado com sucesso"}), 200

if __name__ == "__main__":
    criar_banco()  # Garantir que a tabela exista
    app.run(debug=True)
