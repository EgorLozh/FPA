DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
COMPOSE_FILE = docker-compose.yaml
MANAGE_PY = python app/manage.py
APP_CONTAINER = app

.PHONY: all
all:
	$(DC) -f $(COMPOSE_FILE) up --build -d


.PHONY: down
down:
	$(DC) -f $(COMPOSE_FILE) down


.PHONY: migrations
migrations:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) makemigrations


.PHONY: migrate
migrate:
	$(EXEC) $(APP_CONTAINER) poetry run $(MANAGE_PY) migrate


.PHONY: restart
restart: down all
