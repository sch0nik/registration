start:
	poetry run python manage.py runserver

makemigrations:
		poetry run python manage.py makemigrations

migrate:
		poetry run python manage.py migrate

start-bot:
	poetry run python manage.py run_bot

shell:
	poetry run python manage.py shell

requiremets:
	poetry export -f requirements.txt --output requirements.txt

init: makemigration, migrate
