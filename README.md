# Instruções para Configurar e Rodar o Projeto

## 1. Clonar o Repositório
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>

## 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)
python -m venv venv

## 3. Ativar o Ambiente Virtual
venv\Scripts\activate

## 4. Instalar as Dependências
pip install -r requirements.txt

## 5. Rodar o Servidor
python nome_do_arquivo_principal.py  # substitua pelo nome do arquivo principal, como cadastro_vendas.py ou mod_login.py

## Endpoints Disponíveis

### 1. Login

- **URL**: `/login`
- **Método**: `POST`
- **Corpo da Requisição**:
  ```json
  {
    "email": "velocitqr@gmail.com",
    "senha": "katiau123"
  }


## 2. Cadastro de Vendas
- **URL**: `/cadastrar_venda`
- **Método**: `POST`
 **Corpo da Requisição**:
  ```json
  {
  "Nome": "João Silva",
  "CpfCnpj": "12345678901",
  "Email": "joao.silva@example.com",
  "Telefone": "11987654321",
  "NumeroPeca": "12345"
  }

## 3. Consulta de Produtos
- **URL**: `/pecas_disponiveis`
- **Método**: `GET`

## 4. Cadastro de Peças
- **URL**: `/cadastrar_peca`
- **Método**: `POST`
 **Corpo da Requisição**:
  ```json
  {
  "ModeloPeca": "XYZ123",
  "MarcaPeca": "MarcaX",
  "NumeroPeca": "456789",
  "NumeroLote": "12345"
  }

 ## 5. Consulta de uma Peça
- **URL**: `/consultar_peca`
- **Método**: `POST`
 **Corpo da Requisição**:
  ```json
  {
  "codigo_peca": "FR30083"
  }

- **Resposta de Sucesso**:
- ```json
  {
  "message": "Peça consultada com sucesso!",
  "peca": {
    "Marca": "FRAM",
    "Produto": "Filtro de Óleo",
    "Código da Peça": "FR30083",
    "Número de Lote": "12345"
  }
  }

 


