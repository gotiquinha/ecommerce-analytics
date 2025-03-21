from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json

fake = Faker('pt_BR')

def generate_sample_data(num_records=1000):
    data = []
    
    # Lista de produtos com preços
    produtos = [
        {"nome": "Smartphone", "preco_base": 1500, "categoria": "Eletrônicos"},
        {"nome": "Notebook", "preco_base": 3500, "categoria": "Eletrônicos"},
        {"nome": "Fones de Ouvido", "preco_base": 200, "categoria": "Acessórios"},
        {"nome": "Smart TV", "preco_base": 2500, "categoria": "Eletrônicos"},
        {"nome": "Tablet", "preco_base": 1200, "categoria": "Eletrônicos"},
        {"nome": "Carregador Portátil", "preco_base": 100, "categoria": "Acessórios"},
        {"nome": "Câmera Digital", "preco_base": 1800, "categoria": "Eletrônicos"},
        {"nome": "Mouse Wireless", "preco_base": 80, "categoria": "Acessórios"}
    ]
    
    # Data inicial (6 meses atrás)
    data_inicial = datetime.now() - timedelta(days=180)
    
    for _ in range(num_records):
        produto = random.choice(produtos)
        data_venda = data_inicial + timedelta(
            days=random.randint(0, 180),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
        # Variação aleatória no preço base (±10%)
        preco_final = produto["preco_base"] * (1 + random.uniform(-0.1, 0.1))
        
        quantidade = random.randint(1, 5)
        
        venda = {
            "id_venda": fake.uuid4(),
            "data_venda": data_venda,
            "cliente": {
                "id": fake.uuid4(),
                "nome": fake.name(),
                "email": fake.email(),
                "cidade": fake.city(),
                "estado": fake.state_abbr()
            },
            "produto": {
                "nome": produto["nome"],
                "categoria": produto["categoria"],
                "preco_unitario": round(preco_final, 2)
            },
            "quantidade": quantidade,
            "valor_total": round(preco_final * quantidade, 2),
            "forma_pagamento": random.choice(["Cartão de Crédito", "Boleto", "PIX"]),
            "status": random.choice(["Concluído", "Cancelado", "Em processamento"]),
        }
        data.append(venda)
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sample_data()
    print(f"Dados gerados: {len(df)} registros")
    print("\nPrimeiros registros:")
    print(df.head())
    
    # Salvando em JSON
    with open("data/vendas.json", "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, default=str)
    
    # Convertendo para DataFrame e salvando em CSV
    df.to_csv("data/vendas.csv", index=False) 