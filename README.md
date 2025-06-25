# 📘 EAD Auth User (Python)

Este é um microserviço de autenticação para uma aplicação EAD (Ensino a Distância), construído com foco em escalabilidade, testes automatizados e boas práticas de desenvolvimento com Python.

---

## 🚀 Tecnologias Utilizadas

### ⚙️ Backend

- **Python 3.10** — Linguagem principal do projeto.
- **FastAPI** — Framework web moderno, rápido e com tipagem forte.
- **Pydantic** — Para validação de dados e configuração da aplicação.
- **SQLAlchemy** — ORM para manipulação do banco de dados.
- **Alembic** — Migrations para versionamento do schema do banco.

### 🐘 Banco de Dados

- **PostgreSQL 16 (Alpine)** — Usado tanto em desenvolvimento local quanto nos testes via containers Docker.

### 🧪 Testes

- **Pytest** — Framework principal de testes.
- **pytest-cov** — Para análise de cobertura de testes.
- **pytest-asyncio** — Para testes assíncronos com FastAPI.
- **coverage** — Geração de relatórios de cobertura de código.

### 🛠️ Ferramentas de Qualidade

- **mypy** — Checagem de tipos estáticos em Python.
- **flake8** — Análise de estilo e linting.
- **isort** — Organização e padronização de imports.
- **pre-commit** — Para executar essas ferramentas antes de cada commit.

### 📦 Gerenciamento de Dependências

- **Poetry** — Ferramenta para gerenciamento de pacotes e ambientes virtuais.
- Utilizamos `pyproject.toml` para consolidar todas as configurações.

### 🐳 Docker

- **Docker Compose** — Para orquestrar os serviços como o banco de dados e a API em ambientes de desenvolvimento/teste.
- Comando `make db-up` sobe o container do PostgreSQL.
- Comando `make docker-up` constrói a aplicação em container (com Poetry e dependências).

### 🧪 Testes Automatizados (CI)

- **GitHub Actions** — CI configurado com:
  - Lint e análise de tipo (`make format`, `make type-check`)
  - Execução de testes unitários e de integração
  - Uso de variáveis e secrets via configuração do repositório

---

## 📂 Organização de Comandos

Usamos um `Makefile` para facilitar os comandos do dia a dia:

```bash
make setup            # Instala dependências via poetry
make db-up            # Sobe o PostgreSQL via Docker
make db-create        # Cria o banco, se não existir
make migrate          # Aplica as migrations
make test             # Roda todos os testes com cobertura
make test-unit        # Apenas testes unitários
make test-integration # Apenas testes de integração
make lint             # Verifica formatação (flake8, isort)
make type-check       # Verifica tipos com mypy
```

## 📌 Requisitos
- Python 3.10.13 (recomendado usar pyenv ou asdf para gerenciar)
- Docker + Docker Compose
- Poetry instalado globalmente