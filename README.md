# Sistema de Análise de Vendas E-commerce

Este é um sistema de análise de dados para e-commerce que permite coletar, armazenar e analisar dados de vendas online, gerando insights valiosos para tomada de decisão.

## Funcionalidades

- Geração de dados de exemplo
- Análises estatísticas de vendas
- Visualização interativa com dashboard
- Integração com MongoDB
- Filtros por período
- Métricas importantes como ticket médio e total de vendas
- Gráficos e mapas interativos

## Requisitos

- Python 3.8+
- MongoDB
- Bibliotecas Python (ver requirements.txt)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd ecommerce_analytics
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas configurações:
- Ajuste a URL do MongoDB conforme sua configuração
- Configure outras variáveis de ambiente necessárias

5. Configure o MongoDB:
- Instale o MongoDB em sua máquina ou use Docker
- Inicie o serviço do MongoDB
- Configure a URL de conexão no arquivo .env

## Segurança

### Configuração Inicial
1. Nunca compartilhe seu arquivo `.env`
2. Não commite arquivos sensíveis (já configurados no .gitignore)
3. Use senhas fortes para o MongoDB
4. Configure autenticação no MongoDB

### Boas Práticas
- Mantenha as dependências atualizadas
- Não armazene dados sensíveis no código
- Use variáveis de ambiente para configurações
- Faça backup regular dos dados
- Monitore logs de acesso

## Uso

1. Gere dados de exemplo:
```bash
python src/data_generator.py
```

2. Inicie o dashboard:
```bash
streamlit run src/app.py
```

3. Acesse o dashboard em seu navegador (geralmente em http://localhost:8501)

## Estrutura do Projeto

```
ecommerce_analytics/
├── data/               # Diretório para dados gerados
├── src/               # Código fonte
│   ├── app.py         # Aplicação Streamlit
│   ├── database.py    # Conexão com MongoDB
│   └── data_generator.py  # Gerador de dados
├── requirements.txt    # Dependências
├── .env.example       # Exemplo de configurações
├── .gitignore        # Arquivos ignorados no git
└── README.md          # Este arquivo
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes 