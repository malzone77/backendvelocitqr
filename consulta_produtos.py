from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Caminho completo do arquivo .xlsx
file_path = r'C:\Users\Victor\Desktop\xlsx\Pasta1.xlsx'
pecas_df = pd.read_excel(file_path)

# Exibe as colunas disponíveis para depuração
print(pecas_df.columns)

# Transformar os dados em uma lista de dicionários para fácil acesso
pecas_disponiveis = pecas_df[['Marca', 'Produto', 'Código da Peça', 'Número de Lote']].to_dict(orient='records')
print(pecas_disponiveis)  # Adicione esta linha para depurar

@app.route('/pecas_disponiveis', methods=['GET'])
def listar_pecas():
    """Endpoint para listar as peças disponíveis com base no arquivo .xlsx"""
    return jsonify({"pecas": pecas_disponiveis}), 200

@app.route('/consultar_peca', methods=['GET'])
def consultar_peca():
    """Endpoint para consultar uma peça selecionada"""
    data = request.json
    
    # Extrair e validar a seleção da peça
    codigo_peca = data.get("codigo_peca")
    if not codigo_peca:
        return jsonify({"error": "Código da peça é obrigatório"}), 400
    
    # Verificar se o código da peça está entre as peças disponíveis
    peca_encontrada = next((peca for peca in pecas_disponiveis if peca['Código da Peça'] == codigo_peca), None)
    if not peca_encontrada:
        return jsonify({"error": "Código da peça não encontrado"}), 404
    
    # Consultar a peça (aqui apenas simulado com uma mensagem)
    return jsonify({
        "message": "Peça consultada com sucesso!",
        "peca": peca_encontrada
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
