.PHONY: test

compose=sudo docker compose -f docker-compose.yaml

up:
	$(compose) up --build -d

down:
	$(compose) down

logs:
	$(compose) logs -f --no-log-prefix --tail=1000 web

logs-sql:
	$(compose) logs -f db

migrations:
	$(compose) exec web python manage.py makemigrations

migrate:
	$(compose) exec web python manage.py migrate

shell:
	$(compose) exec web python manage.py shell_plus

createadmin:
	$(compose) exec web python manage.py createsuperuser

test_users:
	$(compose) exec web python manage.py test src.users.tests

test_tasks:
	$(compose) exec web python manage.py test src.tasks.tests