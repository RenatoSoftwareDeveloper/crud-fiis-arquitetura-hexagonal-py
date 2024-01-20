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
|   |-- routes/
|       |-- __init__.py
|       |-- fundo_imobiliario_routes.py  # Rotas da API para CRUD de fundos imobiliários
|
|-- config/
|   |-- __init__.py
|   |-- requirements.txt  # Lista de dependências para o projeto
|
|-- venv/  # Ambiente virtual Python
|-- |-- app.py  # # Ponto de entrada da aplicação
```

### Camada e suas responsabilidades:
1. Camada de Domínio (domain):

- fundo_imobiliario.py (Entidade): Define a estrutura da entidade FundoImobiliario que representa um fundo imobiliário no domínio da aplicação. A entidade contém informações como id, nome, valor e descricao.</br></br>

- fundo_imobiliario_inbound_port.py
(Portas de Entrada): Define os contratos de entrada para as operações do caso de uso. Essas portas são implementadas pela camada de adaptação.</br></br>

- fundo_imobiliario_outbound_port.py 
(Portas de Saída): Define os contratos de saída para as operações do caso de uso. Essas portas são implementadas pela camada de infraestrutura. </br></br>

- fundo_imobiliario_use_case.py (Casos de Uso)
Implementa a lógica de negócios e interação entre as portas de entrada e saída. Realiza operações como listar fundos, obter fundo por ID, criar, atualizar e excluir fundo imobiliário.</br></br>

2. Camada de Adaptação (adapters):
- controller (Controladores): Contém os controladores da interface do usuário. Recebe solicitações da API, chama os casos de uso correspondentes e retorna as respostas adequadas.</br></br>

- request (Classes de Solicitação): Define classes que representam os dados recebidos nas solicitações da interface do usuário.</br></br>

- response (Classes de Resposta): Define classes que representam as respostas enviadas pela interface do usuário.</br></br>

3. Camada de Infraestrutura (infrastructure):
- fundo_imobiliario_repository.py (Repositório): Implementa as operações de persistência para a entidade FundoImobiliario. Neste exemplo, utiliza uma estrutura de dados em memória para simular um repositório de banco de dados.</br></br>

4. Camada da Web (web): 
- routes (Rotas da API): Define as rotas da API usando o framework Flask. Mapeia as operações CRUD para os métodos HTTP e chama os controladores correspondentes. </br></br>

5. Ponto de Entrada (app.py):
- app.py (Ponto de Entrada): Inicializa a aplicação Flask e registra as rotas da API. </br></br>

Cada camada tem responsabilidades bem definidas e segue os princípios da Arquitetura Hexagonal, também conhecida como Arquitetura Ports and Adapters. 
Isso facilita a manutenção, testabilidade e evolução do sistema, pois as dependências estão claramente definidas entre as camadas.