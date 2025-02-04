run: ## Запуск приложения
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .local.env

install: ## Установка приложений
	@echo "Установка зависимостей библиотеки - $(LIB)"
	poetry add $(LIB)

uninstall: ## Удаление зависимостей
	@echo "Удаление зависимостей библиотеки - $(LIB)"
	poetry remove $(LIB)


migrate:
	alembic revision --autogenerate -m $(TEXT)


migrate-apply:
	alembic upgrade head


migrate-history:
	alembic history --verbose


migrate-downgrade-base:
	alembic downgrade base


migrate-downgrade-revision:
	alembic downgrade $(R)  