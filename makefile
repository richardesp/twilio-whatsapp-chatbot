APP=main:app
HOST=0.0.0.0
PORT=8000
RELOAD=--reload
APP_DIR=app

dev:
	@export LOG_LEVEL=debug; \
	uvicorn $(APP) --host $(HOST) --port $(PORT) $(RELOAD) --log-level $$LOG_LEVEL --app-dir $(APP_DIR)

prod:
	@export LOG_LEVEL=info; \
	uvicorn $(APP) --host $(HOST) --port $(PORT) --log-level $$LOG_LEVEL --app-dir $(APP_DIR)

ngrok:
	ngrok http $(PORT)