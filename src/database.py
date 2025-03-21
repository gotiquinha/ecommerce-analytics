from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        self.db = self.client['ecommerce_analytics']
        self.vendas = self.db['vendas']
    
    def insert_sales_data(self, data):
        """Insere dados de vendas no MongoDB"""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict('records')
        return self.vendas.insert_many(data)
    
    def get_sales_by_period(self, start_date, end_date):
        """Retorna vendas em um período específico"""
        query = {
            "data_venda": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
        return list(self.vendas.find(query))
    
    def get_top_products(self, limit=10):
        """Retorna os produtos mais vendidos"""
        pipeline = [
            {
                "$group": {
                    "_id": "$produto.nome",
                    "total_vendas": {"$sum": "$quantidade"},
                    "valor_total": {"$sum": "$valor_total"}
                }
            },
            {"$sort": {"total_vendas": -1}},
            {"$limit": limit}
        ]
        return list(self.vendas.aggregate(pipeline))
    
    def get_average_ticket(self):
        """Calcula o ticket médio"""
        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "ticket_medio": {"$avg": "$valor_total"}
                }
            }
        ]
        result = list(self.vendas.aggregate(pipeline))
        return result[0] if result else None
    
    def get_sales_by_payment_method(self):
        """Retorna vendas por método de pagamento"""
        pipeline = [
            {
                "$group": {
                    "_id": "$forma_pagamento",
                    "total_vendas": {"$sum": 1},
                    "valor_total": {"$sum": "$valor_total"}
                }
            }
        ]
        return list(self.vendas.aggregate(pipeline))
    
    def get_sales_by_state(self):
        """Retorna vendas por estado"""
        pipeline = [
            {
                "$group": {
                    "_id": "$cliente.estado",
                    "total_vendas": {"$sum": 1},
                    "valor_total": {"$sum": "$valor_total"}
                }
            }
        ]
        return list(self.vendas.aggregate(pipeline))

if __name__ == "__main__":
    # Teste de conexão
    db = DatabaseConnection()
    print("Conexão com MongoDB estabelecida com sucesso!") 