# 🏡 CRUD de Fundos Imobiliários com Arquitetura Hexagonal em Python
- Este projeto é um CRUD (Create, Read, Update, Delete) de Fundos Imobiliários implementado em Python, adotando a arquitetura hexagonal para promover modularidade e manutenibilidade do código. A arquitetura hexagonal, também conhecida como Ports and Adapters, separa as preocupações de negócios das implementações técnicas, facilitando a escalabilidade e testabilidade do sistema.

# Tecnologias Utilizadas
* Python 🐍: Linguagem de programação principal do projeto.
* Arquitetura Hexagonal 🔺: Abordagem arquitetônica que promove organização e separação de responsabilidades.
* VS Code 💻: Ambiente de desenvolvimento integrado utilizado para codificação.
* Flask 🌐: Framework web leve para construção de aplicativos web.
* SQLAlchemy 🗃️: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados.
* Flask-RESTful 🚀: Extensão do Flask para construção de APIs RESTful.

### Pré-requisitos
- Python: https://www.python.org/
- VS Code: https://code.visualstudio.com/

### venv
- Configurar um ambiente virtual no Python é uma prática recomendada para isolar as dependências do seu projeto.

* python -m venv venv
* .\venv\Scripts\activate
* deactivate

###  Dependências do projetos 
- cd crud
- pip install -r config/requirements.txt

### Configuração do Ambiente de Desenvolvimento
1. Clone o repositório: git clone ```https://github.com/seu-usuario/seu-projeto.git```
2. Acesse o diretório do projeto: ```cd seu-projeto```
3. Instale as dependências: ```pip install -r requirements.txt ```
### Como Executar
1- Abra o VS Code no diretório do projeto.
2- Execute o aplicativo Flask: python app.py
3- Acesse a API em http://localhost:5000
### Funcionalidades
- Listar Fundos Imobiliários: Endpoint para listar todos os fundos cadastrados.
- Detalhes de um Fundo: Endpoint para obter detalhes de um fundo específico.
- Adicionar Fundo Imobiliário: Endpoint para adicionar um novo fundo ao sistema.
- Atualizar Fundo Imobiliário: Endpoint para atualizar informações de um fundo existente.
- Remover Fundo Imobiliário: Endpoint para remover um fundo do sistema.

### Contribuições
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Estrutura do projeto:
```
crud/
|-- adapters/
|   |-- __init__.py
|   |-- controller/
|   |   |-- __init__.py
|   |   |-- fundo_imobiliario_controller.py  # Controladores da interface do usuário
|   |
|   |-- request/
|   |   |-- __init__.py
|   |   |-- fundo_imobiliario_request.py  # Classes para representar as solicitações da interface do usuário
|   |
|   |-- response/
|       |-- __init__.py
|       |-- fundo_imobiliario_response.py  # Classes para representar as respostas da interface do usuário
|
|-- domain/
|   |-- __init__.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- fundo_imobiliario.py  # Entidades e objetos de valor do domínio
|   |
|   |-- ports/
|       |-- __init__.py
|       |-- inbound/
|       |   |-- __init__.py
|       |   |-- fundo_imobiliario_inbound_port.py  # Contratos de entrada definidos pela camada de domínio
|       |
|       |-- outbound/
|           |-- __init__.py
|           |-- fundo_imobiliario_outbound_port.py  # Contratos de saída definidos pela camada de domínio
|   |
|   |-- use_cases/
|       |-- __init__.py
|       |-- fundo_imobiliario_use_case.py  # Casos de uso da aplicação definidos pela camada de domínio, referenciando as portas
|
|-- infrastructure/
|   |-- __init__.py
|   |-- repositories/
|       |-- __init__.py
|       |-- fundo_imobiliario_repository.py  # Implementação do repositório, interação com banco de dados ou armazenamento
|-- web/
|   |-- __init__.py
|   |-- app.py  # # Ponto de entrada da aplicação
|   |-- routes/
|       |-- __init__.py
|       |-- fundo_imobiliario_routes.py  # Rotas da API para CRUD de fundos imobiliários
|
|-- config/
|   |-- __init__.py
|   |-- requirements.txt  # Lista de dependências para o projeto
|
|-- venv/  # Ambiente virtual Python
|-- run.py  # Script para iniciar a aplicação
```