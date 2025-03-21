# Sistema de Análise de Vendas E-commerce

## Visão Geral
Este projeto consiste em um sistema de análise de dados para e-commerce que coleta, armazena e analisa dados de vendas online, gerando insights valiosos para tomada de decisão através de um dashboard interativo.

## Objetivo
O principal objetivo é fornecer uma ferramenta que permita visualizar e analisar dados de vendas de forma clara e intuitiva, auxiliando gestores e analistas na tomada de decisões estratégicas baseadas em dados.

## Tecnologias Utilizadas

### Backend
- **Python 3.12**: Escolhido por sua robustez em análise de dados e vasta biblioteca de pacotes científicos
- **MongoDB**: Banco de dados NoSQL que oferece flexibilidade para armazenar dados em formato JSON e realizar consultas complexas
- **PyMongo**: Biblioteca Python para integração com MongoDB, permitindo operações eficientes no banco de dados
- **Docker**: Utilizado para containerização do MongoDB, garantindo consistência entre ambientes e facilidade de implantação

### Análise de Dados
- **Pandas**: Biblioteca Python para manipulação e análise de dados, oferecendo estruturas de dados eficientes e ferramentas de análise
- **NumPy**: Biblioteca fundamental para computação numérica em Python, utilizada para cálculos estatísticos

### Frontend/Visualização
- **Streamlit**: Framework para criação de aplicações web com Python, escolhido pela facilidade de desenvolvimento e foco em dados
- **Plotly**: Biblioteca de visualização de dados que oferece gráficos interativos e responsivos
- **Plotly Express**: API de alto nível do Plotly para criação rápida de visualizações complexas

### Utilitários
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **Faker**: Geração de dados fictícios para demonstração e testes

## Arquitetura do Sistema

### Estrutura de Diretórios
```
ecommerce_analytics/
├── data/               # Dados gerados
├── src/               
│   ├── app.py         # Aplicação Streamlit
│   ├── database.py    # Conexão com MongoDB
│   └── data_generator.py  # Gerador de dados
├── requirements.txt    # Dependências
├── .env               # Configurações
└── README.md          # Documentação básica
```

### Componentes Principais

1. **Gerador de Dados (`data_generator.py`)**
   - Gera dados fictícios de vendas
   - Simula transações com variação de preços e quantidades
   - Cria registros com informações de clientes e produtos

2. **Conexão com Banco de Dados (`database.py`)**
   - Gerencia conexão com MongoDB
   - Implementa queries para análise de dados
   - Fornece interface para inserção e consulta de dados

3. **Dashboard (`app.py`)**
   - Interface interativa com filtros de período
   - Visualizações:
     - Métricas principais (KPIs)
     - Gráficos de vendas por produto
     - Distribuição por forma de pagamento
     - Mapa geográfico de vendas
     - Tabela detalhada com filtros

## Funcionalidades

### Análises Estatísticas
- Total de vendas por período
- Ticket médio
- Produtos mais vendidos
- Taxa de conclusão de vendas
- Distribuição geográfica

### Visualizações
- Gráficos de barras para análise de produtos
- Gráficos de pizza para distribuição de pagamentos
- Mapa interativo com dados por estado
- Tabelas dinâmicas com filtros

### Filtros e Interatividade
- Seleção de período de análise
- Filtros por status de venda
- Filtros por forma de pagamento
- Ordenação de dados em tabelas

## Implantação
O sistema utiliza Docker para garantir a portabilidade e facilidade de implantação. O MongoDB é executado em um container, permitindo fácil escalabilidade e manutenção.

## Segurança
- Variáveis sensíveis armazenadas em arquivo .env
- Conexão segura com o banco de dados
- Dados sensíveis de clientes são simulados

## Próximos Passos
1. Implementação de autenticação de usuários
2. Adição de mais análises preditivas
3. Exportação de relatórios em PDF
4. Integração com APIs de e-commerce reais
5. Implementação de alertas automáticos 