DC = docker compose
EXEC = docker exec -it
ENV_FILE = .env
LOGS = docker logs
BACK_COMPOSE_FILE = docker_compose/backend_app.yaml
DB_COMPOSE_FILE = docker_compose/db.yaml
MANAGE_PY = python app/manage.py
APP_CONTAINER = app

.PHONY: all
all:
	$(DC) --env-file $(ENV_FILE) -f $(BACK_COMPOSE_FILE) -f $(DB_COMPOSE_FILE) up --build -d


.PHONY: down
down:
	$(DC) -f $(BACK_COMPOSE_FILE) -f $(DB_COMPOSE_FILE) down


.PHONY: migrations
migrations:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) makemigrations


.PHONY: migrate
migrate:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) migrate


.PHONY: restart
restart: down all
