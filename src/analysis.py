import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df
        
    def vendas_por_periodo(self, periodo='M'):
        """Análise de vendas por período (D=diário, M=mensal, Y=anual)"""
        self.df['data_venda'] = pd.to_datetime(self.df['data_venda'])
        vendas = self.df.set_index('data_venda').resample(periodo)['valor_total'].sum()
        return vendas
    
    def produtos_mais_vendidos(self, top_n=10):
        """Retorna os produtos mais vendidos"""
        return self.df.groupby('produto.nome').agg({
            'quantidade': 'sum',
            'valor_total': 'sum'
        }).sort_values('quantidade', ascending=False).head(top_n)
    
    def ticket_medio(self):
        """Calcula o ticket médio"""
        return self.df['valor_total'].mean()
    
    def vendas_por_categoria(self):
        """Análise de vendas por categoria"""
        return self.df.groupby('produto.categoria')['valor_total'].sum()
    
    def metodos_pagamento(self):
        """Análise dos métodos de pagamento"""
        return self.df['metodo_pagamento'].value_counts()
    
    def vendas_por_estado(self):
        """Análise de vendas por estado"""
        return self.df.groupby('cliente.estado')['valor_total'].sum() 