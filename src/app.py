import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from database import DatabaseConnection
from datetime import datetime, timedelta
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Dashboard E-commerce",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
        .main > div {
            padding: 2rem;
        }
        .stMetric {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stPlotlyChart {
            background-color: white;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .dataframe {
            font-size: 14px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Inicialização da conexão com o banco de dados
db = DatabaseConnection()

def format_currency(value):
    """Formata valores monetários com 2 casas decimais"""
    return f"R$ {value:,.2f}".replace('.', '#').replace(',', '.').replace('#', ',')

def format_table_data(df):
    """Formata os dados da tabela para melhor visualização"""
    df_formatted = df.copy()
    
    # Formatando data
    df_formatted['data_venda'] = pd.to_datetime(df_formatted['data_venda']).dt.strftime('%d/%m/%Y %H:%M')
    
    # Formatando valores monetários
    df_formatted['valor_total'] = df_formatted['valor_total'].apply(format_currency)
    if 'produto' in df_formatted.columns:
        df_formatted['produto'] = df_formatted['produto'].apply(
            lambda x: f"{x['nome']} - {format_currency(x['preco_unitario'])}"
        )
    
    # Formatando informações do cliente
    if 'cliente' in df_formatted.columns:
        df_formatted['cliente'] = df_formatted['cliente'].apply(
            lambda x: f"{x['nome']} ({x['cidade']}-{x['estado']})"
        )
    
    # Selecionando e renomeando colunas
    colunas_exibir = {
        'data_venda': 'Data da Venda',
        'cliente': 'Cliente',
        'produto': 'Produto',
        'quantidade': 'Quantidade',
        'valor_total': 'Valor Total',
        'forma_pagamento': 'Forma de Pagamento',
        'status': 'Status'
    }
    
    df_formatted = df_formatted[colunas_exibir.keys()].rename(columns=colunas_exibir)
    return df_formatted

def get_state_info():
    """Retorna dicionário com informações dos estados"""
    return {
        'AC': {'nome': 'Acre', 'latitude': -8.77, 'longitude': -70.55},
        'AL': {'nome': 'Alagoas', 'latitude': -9.62, 'longitude': -36.82},
        'AM': {'nome': 'Amazonas', 'latitude': -3.47, 'longitude': -65.10},
        'AP': {'nome': 'Amapá', 'latitude': 1.41, 'longitude': -51.77},
        'BA': {'nome': 'Bahia', 'latitude': -12.96, 'longitude': -41.68},
        'CE': {'nome': 'Ceará', 'latitude': -5.20, 'longitude': -39.53},
        'DF': {'nome': 'Distrito Federal', 'latitude': -15.83, 'longitude': -47.86},
        'ES': {'nome': 'Espírito Santo', 'latitude': -19.19, 'longitude': -40.34},
        'GO': {'nome': 'Goiás', 'latitude': -15.98, 'longitude': -49.86},
        'MA': {'nome': 'Maranhão', 'latitude': -5.42, 'longitude': -45.44},
        'MT': {'nome': 'Mato Grosso', 'latitude': -12.64, 'longitude': -55.42},
        'MS': {'nome': 'Mato Grosso do Sul', 'latitude': -20.51, 'longitude': -54.54},
        'MG': {'nome': 'Minas Gerais', 'latitude': -18.10, 'longitude': -44.38},
        'PA': {'nome': 'Pará', 'latitude': -3.79, 'longitude': -52.48},
        'PB': {'nome': 'Paraíba', 'latitude': -7.28, 'longitude': -36.72},
        'PR': {'nome': 'Paraná', 'latitude': -24.89, 'longitude': -51.55},
        'PE': {'nome': 'Pernambuco', 'latitude': -8.38, 'longitude': -37.86},
        'PI': {'nome': 'Piauí', 'latitude': -6.60, 'longitude': -42.28},
        'RJ': {'nome': 'Rio de Janeiro', 'latitude': -22.25, 'longitude': -42.66},
        'RN': {'nome': 'Rio Grande do Norte', 'latitude': -5.81, 'longitude': -36.59},
        'RO': {'nome': 'Rondônia', 'latitude': -10.83, 'longitude': -63.34},
        'RS': {'nome': 'Rio Grande do Sul', 'latitude': -30.17, 'longitude': -53.50},
        'RR': {'nome': 'Roraima', 'latitude': 1.99, 'longitude': -61.33},
        'SC': {'nome': 'Santa Catarina', 'latitude': -27.45, 'longitude': -50.95},
        'SE': {'nome': 'Sergipe', 'latitude': -10.57, 'longitude': -37.45},
        'SP': {'nome': 'São Paulo', 'latitude': -22.19, 'longitude': -48.79},
        'TO': {'nome': 'Tocantins', 'latitude': -9.46, 'longitude': -48.26}
    }

def main():
    st.title("📊 Dashboard de Análise de Vendas")
    
    # Sidebar com filtros
    st.sidebar.header("Filtros")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        data_inicial = st.date_input(
            "Data Inicial",
            datetime.now() - timedelta(days=180)
        )
    with col2:
        data_final = st.date_input(
            "Data Final",
            datetime.now()
        )
    
    # Convertendo date para datetime
    data_inicial = datetime.combine(data_inicial, datetime.min.time())
    data_final = datetime.combine(data_final, datetime.max.time())
    
    # Obtendo dados filtrados
    vendas = db.get_sales_by_period(data_inicial, data_final)
    df_vendas = pd.DataFrame(vendas)
    
    if df_vendas.empty:
        st.warning("Nenhum dado encontrado para o período selecionado.")
        return
    
    # Métricas principais em cards
    st.markdown("### Métricas Principais")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_vendas = df_vendas['valor_total'].sum()
        st.metric("Total de Vendas", format_currency(total_vendas))
    
    with col2:
        ticket_medio = db.get_average_ticket()
        if ticket_medio:
            st.metric("Ticket Médio", format_currency(ticket_medio['ticket_medio']))
    
    with col3:
        num_vendas = len(df_vendas)
        st.metric("Número de Vendas", f"{num_vendas:,}")
    
    with col4:
        taxa_conclusao = (df_vendas['status'] == 'Concluído').mean() * 100
        st.metric("Taxa de Conclusão", f"{taxa_conclusao:.1f}%")
    
    # Gráficos em duas colunas
    st.markdown("### Análise de Vendas")
    col1, col2 = st.columns(2)
    
    with col1:
        produtos = db.get_top_products()
        df_produtos = pd.DataFrame(produtos)
        if not df_produtos.empty:
            fig = px.bar(
                df_produtos,
                x="_id",
                y="total_vendas",
                title="Top Produtos por Quantidade",
                labels={"_id": "Produto", "total_vendas": "Quantidade"},
                template="plotly_white"
            )
            fig.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        pagamentos = db.get_sales_by_payment_method()
        df_pagamentos = pd.DataFrame(pagamentos)
        if not df_pagamentos.empty:
            fig = px.pie(
                df_pagamentos,
                values="valor_total",
                names="_id",
                title="Distribuição por Forma de Pagamento",
                template="plotly_white"
            )
            fig.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Mapa de vendas
    st.markdown("### Distribuição Geográfica")
    vendas_estado = db.get_sales_by_state()
    df_estados = pd.DataFrame(vendas_estado)
    
    if not df_estados.empty:
        # Preparar dados para o mapa
        estados_info = get_state_info()
        df_estados = df_estados.rename(columns={'_id': 'estado'})
        
        # Adicionar informações dos estados
        df_estados['nome_estado'] = df_estados['estado'].map(lambda x: estados_info[x]['nome'])
        df_estados['latitude'] = df_estados['estado'].map(lambda x: estados_info[x]['latitude'])
        df_estados['longitude'] = df_estados['estado'].map(lambda x: estados_info[x]['longitude'])
        
        # Criar mapa com scatter
        fig = go.Figure()

        # Adicionar o mapa base do Brasil
        fig.add_trace(go.Scattergeo(
            lon=df_estados['longitude'],
            lat=df_estados['latitude'],
            text=df_estados.apply(
                lambda row: f"{row['nome_estado']}<br>Vendas: {format_currency(row['valor_total'])}", 
                axis=1
            ),
            mode='markers',
            marker=dict(
                size=df_estados['valor_total'] / df_estados['valor_total'].max() * 50,
                color=df_estados['valor_total'],
                colorscale='Viridis',
                showscale=True,
                colorbar_title="Valor Total de Vendas"
            ),
            hoverinfo='text'
        ))

        # Configurar o layout
        fig.update_layout(
            title='Vendas por Estado',
            geo=dict(
                scope='south america',
                projection_type='mercator',
                showland=True,
                landcolor='rgb(243, 243, 243)',
                countrycolor='rgb(204, 204, 204)',
                showocean=True,
                oceancolor='rgb(230, 230, 250)',
                showcoastlines=True,
                coastlinecolor='rgb(128, 128, 128)',
                center=dict(lat=-15.7801, lon=-47.9292),  # Centro em Brasília
                lataxis=dict(range=[-33, 5]),  # Ajuste para mostrar todo o Brasil
                lonaxis=dict(range=[-75, -35]),
            ),
            height=600,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabela complementar com os valores por estado
        st.markdown("#### Detalhamento por Estado")
        df_display = df_estados[['nome_estado', 'total_vendas', 'valor_total']].copy()
        df_display['valor_total'] = df_display['valor_total'].apply(format_currency)
        df_display.columns = ['Estado', 'Total de Vendas', 'Valor Total']
        st.dataframe(
            df_display.sort_values('Total de Vendas', ascending=False),
            use_container_width=True,
            height=300
        )
    
    # Tabela detalhada com filtro
    st.markdown("### Detalhamento das Vendas")
    if not df_vendas.empty:
        df_display = format_table_data(df_vendas)
        
        # Adicionar filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            status_filter = st.multiselect(
                "Filtrar por Status",
                options=sorted(df_display['Status'].unique())
            )
        with col2:
            pagamento_filter = st.multiselect(
                "Filtrar por Forma de Pagamento",
                options=sorted(df_display['Forma de Pagamento'].unique())
            )
        
        # Aplicar filtros
        if status_filter:
            df_display = df_display[df_display['Status'].isin(status_filter)]
        if pagamento_filter:
            df_display = df_display[df_display['Forma de Pagamento'].isin(pagamento_filter)]
        
        # Exibir tabela
        st.dataframe(
            df_display,
            use_container_width=True,
            height=400
        )

if __name__ == "__main__":
    main() 