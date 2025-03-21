import json
from database import DatabaseConnection
from datetime import datetime

def load_data():
    # Conectar ao MongoDB
    db = DatabaseConnection()
    
    # Ler o arquivo JSON
    with open('data/vendas.json', 'r', encoding='utf-8') as f:
        vendas = json.load(f)
    
    # Converter strings de data para objetos datetime
    for venda in vendas:
        venda['data_venda'] = datetime.fromisoformat(venda['data_venda'].replace('Z', '+00:00'))
    
    # Inserir dados no MongoDB
    result = db.insert_sales_data(vendas)
    print(f"Dados inseridos com sucesso! {len(vendas)} registros inseridos.")

if __name__ == "__main__":
    load_data() 