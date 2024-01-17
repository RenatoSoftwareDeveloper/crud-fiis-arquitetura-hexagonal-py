### Estamos evoluindo o mostrinho  😅😅
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