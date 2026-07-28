HOST ?= 0.0.0.0
PORT ?= 8000

run:
	uvicorn main:app --host $(HOST) --port $(PORT) --reload


migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)


migrate-apply:
	alembic upgrade head