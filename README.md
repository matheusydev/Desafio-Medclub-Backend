<div align="center">

# 🏥 Desafio Medclub Backend

### API REST para gerenciamento de consultas médicas

O objetivo da API é permitir que o aplicativo mobile possa **agendar, visualizar, atualizar e remover consultas médicas** de forma simples e organizada.

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

</div>

---

## 📋 Funcionalidades

- Listagem de todas as consultas cadastradas
- Detalhamento de uma consulta específica por ID
- Cadastro de novas consultas médicas
- Atualização de consultas existentes
- Remoção de consultas agendadas
- Documentação interativa via Swagger

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.13+ | Linguagem principal |
| Django | 5.2.14 | Framework web |
| Django REST Framework | 3.17.1 | Construção da API REST |
| drf-spectacular | latest | Documentação Swagger/OpenAPI |
| python-decouple | latest | Variáveis de ambiente |
| SQLite | — | Banco de dados |

---

## 🔧 Acesso ao Painel Administrativo

URL: http://127.0.0.1:8000/admin/

| Campo | Valor |
|---|---|
| Usuário | adminmedclub |
| Senha | desafio1981 |

## 🗺️ Endpoints da API

Base URL: `http://127.0.0.1:8000/api/`

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/consultas/` | Lista todas as consultas |
| `POST` | `/api/consultas/` | Cadastra uma nova consulta |
| `GET` | `/api/consultas/{id}/` | Retorna detalhes de uma consulta |
| `PUT` | `/api/consultas/{id}/` | Atualiza uma consulta existente |
| `PATCH` | `/api/consultas/{id}/` | Atualiza parcialmente uma consulta |
| `DELETE` | `/api/consultas/{id}/` | Remove uma consulta |

### Exemplo de payload (POST/PUT):

```json
{
  "data": "2026-05-20",
  "hora": "10:30:00",
  "nome_medico": "Dr. Matheus",
  "especialidade": "Cardiologista",
  "localizacao": "Medclub Centro"
}
```

### Exemplo de resposta (GET):

```json
[
  {
    "id": 1,
    "data": "2026-05-20",
    "hora": "10:30:00",
    "nome_medico": "Dr. Matheus",
    "especialidade": "Cardiologista",
    "localizacao": "Medclub Centro"
  }
]
```

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos

- Python 3.13 ou superior
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/matheusydev/Desafio-Medclub-Backend.git

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Instale as dependências
pip install -r requirements.txt
```

### Configuração das Variáveis de Ambiente

```bash
# Crie o arquivo .env na raiz do projeto
# Utilize o .env.example como referência
cp .env.example .env
```

Edite o `.env` com suas configurações:

```bash
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
```

### Execução

```bash
# Aplique as migrations
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/api/`

---

## 🧪 Como Testar a API

### Opção 1 — Swagger 

Acesse a documentação interativa no navegador:

```
http://127.0.0.1:8000/api/docs/
```

Pelo Swagger você pode testar todos os endpoints diretamente no navegador, sem precisar de nenhuma ferramenta adicional.

### Opção 2 — Browsable API do DRF

O Django REST Framework oferece uma interface navegável automática:

```
http://127.0.0.1:8000/api/consultas/
```

### Opção 3 — Postman 

Importe a coleção ou crie requisições manualmente apontando para:

```
http://127.0.0.1:8000/api/consultas/
```

---

## 📁 Estrutura de Pastas

```bash
Desafio_Medclub_Backend/
├── Desafio_Medclub_Backend/    # Configurações do projeto
│   ├── settings.py             # Configurações gerais + DRF + Swagger
│   ├── urls.py                 # Rotas globais do projeto
│   ├── wsgi.py
│   └── asgi.py
│
├── consultas/                  # App principal
│   ├── migrations/             # Histórico de migrações do banco
│   ├── models.py               # Model Consulta com campos da entidade
│   ├── serializers.py          # Serializer para conversão Model ↔ JSON
│   ├── views.py                # ViewSet com CRUD completo e Swagger docs
│   ├── urls.py                 # Rotas do app com DefaultRouter
│   └── admin.py                # Registro do model no painel admin
│
├── .env                        # Variáveis de ambiente (não versionado)
├── .env.example                # Exemplo de variáveis de ambiente
├── .gitignore
├── db.sqlite3                  # Banco de dados SQLite
├── manage.py
└── requirements.txt            # Dependências do projeto
```

---

## 📄 Responsabilidade de cada arquivo

### `models.py`
Define a entidade `Consulta` com os campos: `data`, `hora`, `nome_medico`, `especialidade` e `localizacao`. Inclui o método `__str__` para representação legível no admin.

### `serializers.py`
Responsável pela conversão entre o Model Django e JSON. Utiliza `ModelSerializer` para serialização automática de todos os campos.

### `views.py`
Implementa o `ConsultaViewSet` herdando de `ModelViewSet`, entregando o CRUD completo em poucas linhas. Cada ação é documentada com `@extend_schema` do drf-spectacular.

### `urls.py` (consultas)
Configura as rotas do app utilizando `DefaultRouter`, que gera automaticamente todos os endpoints REST a partir do ViewSet.

### `urls.py` (projeto)
Centraliza as rotas globais, incluindo as rotas do app com prefixo `api/` e as rotas do Swagger.

### `settings.py`
Configura o Django, DRF, drf-spectacular e as variáveis de ambiente via python-decouple.

---

## 🧠 Decisões Técnicas

### ModelViewSet para CRUD completo
O `ModelViewSet` foi escolhido por gerar automaticamente os 5 endpoints REST (`list`, `create`, `retrieve`, `update`, `destroy`) com pouquíssimo código, seguindo as melhores práticas do DRF.

### DefaultRouter para roteamento
O `DefaultRouter` elimina a necessidade de registrar cada endpoint manualmente, gerando todas as rotas a partir de um único `router.register()`.

### ModelSerializer para serialização
O `ModelSerializer` foi escolhido por inferir automaticamente os campos do Model, reduzindo código repetitivo e mantendo consistência entre Model e API.

### drf-spectacular para documentação
Gera documentação Swagger/OpenAPI automaticamente a partir do código, sem necessidade de manutenção manual. Cada endpoint é descrito com `@extend_schema`.

### python-decouple para variáveis de ambiente
Separa configurações sensíveis (como `SECRET_KEY`) do código-fonte, impedindo que dados críticos sejam expostos no repositório.

### SQLite como banco de dados
Utilizado por ser nativo do Django e suficiente para o escopo do desafio, sem necessidade de configuração adicional.

---

## 🎓 Aprendizados Adquiridos

- ✅ **Django REST Framework** para construção de APIs REST
- ✅ **ModelSerializer** para serialização automática de Models
- ✅ **ModelViewSet** para CRUD completo com mínimo de código
- ✅ **DefaultRouter** para roteamento automático de endpoints
- ✅ **drf-spectacular** para documentação Swagger/OpenAPI
- ✅ **python-decouple** para gerenciamento de variáveis de ambiente
- ✅ **Migrations** para versionamento do banco de dados
- ✅ **Boas práticas REST** como prefixo `api/` e recursos no plural
- ✅ **Conventional Commits** para padronização do histórico do git
- ✅ **Separação de responsabilidades** entre models, serializers, views e urls

---
