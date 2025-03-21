from pymongo import MongoClient
import json
from datetime import datetime

def test_mongodb_connection():
    try:
        # Tentar conectar ao MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Verificar se consegue fazer ping no servidor
        client.admin.command('ping')
        
        print("Conexão com MongoDB estabelecida com sucesso!")
        
        # Criar/acessar o banco de dados
        db = client['ecommerce_analytics']
        
        # Criar/acessar a coleção
        vendas = db['vendas']
        
        # Inserir um documento de teste
        venda_teste = {
            "id_venda": "teste123",
            "data_venda": datetime.now(),
            "cliente": {
                "nome": "Cliente Teste",
                "email": "teste@teste.com",
                "cidade": "São Paulo",
                "estado": "SP"
            },
            "produto": {
                "nome": "Produto Teste",
                "categoria": "Teste",
                "preco_unitario": 100.00
            },
            "quantidade": 1,
            "valor_total": 100.00,
            "forma_pagamento": "Cartão de Crédito",
            "status": "Concluído"
        }
        
        result = vendas.insert_one(venda_teste)
        print(f"Documento de teste inserido com ID: {result.inserted_id}")
        
        # Verificar se consegue recuperar o documento
        doc = vendas.find_one({"id_venda": "teste123"})
        if doc:
            print("Documento recuperado com sucesso!")
            print("\nConteúdo do documento:")
            print(json.dumps(
                {k: str(v) if isinstance(v, datetime) else v 
                 for k, v in doc.items() if k != '_id'}, 
                indent=2, 
                ensure_ascii=False
            ))
        
        # Contar documentos na coleção
        total_docs = vendas.count_documents({})
        print(f"\nTotal de documentos na coleção: {total_docs}")
        
    except Exception as e:
        print(f"Erro ao conectar com MongoDB: {str(e)}")

if __name__ == "__main__":
    test_mongodb_connection() 