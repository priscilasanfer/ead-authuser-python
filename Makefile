SERVICE_NAME := ead-auth-user-python
POETRY_VERSION := 1.8.2
MIN_CODE_COVERAGE := 90
APP_FOLDER := build/app/$(SERVICE_NAME)
LAYER_FOLDER := build/layer/dependencies/python

# =============================================================================
# 🏗️ Setup
# =============================================================================
setup: poetry-install

poetry-install:
	@echo "Instalando dependências com Poetry..."
	pip install poetry==$(POETRY_VERSION) || true
	poetry install

# =============================================================================
# 🚀 Aplication
# =============================================================================
run:
	poetry run uvicorn app.main:app --reload

shell:
	poetry run python

# =============================================================================
# 🐳 Docker and Database
# =============================================================================
db-up:
	docker compose up -d postgres

db-down:
	docker compose stop postgres

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f
# =============================================================================
# 🗄️ Build Lambda Layer/Package
# =============================================================================
build:
	pip install poetry-plugin-export
	mkdir -p $(LAYER_FOLDER)
	poetry export --without-hashes -f requirements.txt > requirements.txt
	poetry run pip install -r requirements.txt -t $(LAYER_FOLDER)
	rm -f requirements.txt
	mkdir -p $(APP_FOLDER)
	cp -rf app $(APP_FOLDER)

# =============================================================================
# 📜 Migrations
# =============================================================================
migrate:
	poetry run alembic upgrade head

makemigrations:
	poetry run alembic revision --autogenerate -m "$(message)"

manual-migration:
	poetry run alembic revision -m "$(message)"

# =============================================================================
# 🧪 Tests
# =============================================================================
test:
	poetry run pytest tests

test-unit:
	poetry run pytest tests/unit --cov=. --cov-report=term --cov-report=html --cov-fail-under=$(MIN_CODE_COVERAGE)

test-integration:
	poetry run pytest tests/integration

test-e2e:
	poetry run pytest tests/e2e

# =============================================================================
# 🔍 Code Quality
# =============================================================================
format:
	poetry run flake8
	poetry run isort .
	poetry run black .
	poetry run unimport .

type-check:
	poetry run mypy .

security:
	poetry run bandit -c bandit.yml -r app tests

pre-commit:
	poetry run pre-commit run --all-files

check: format type-check security test

# =============================================================================
# 🏁 Utility
# =============================================================================
check: format security test

clean:
	rm -rf __pycache__ .pytest_cache build dist *.egg-info .mypy_cache

# =============================================================================
# 🎯 Meta Targets
# =============================================================================
.PHONY: setup poetry-install run shell \
	db-up db-down docker-up docker-down \
	build migrate makemigrations manual-migration \
	test test-unit test-integration test-e2e \
	format security check clean
