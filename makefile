APP = main:app
HOST = 0.0.0.0
PORT = 8000
RELOAD = --reload
LOG_LEVEL_DEV = debug
LOG_LEVEL_PROD = info
APP_DIR = app


dev:
	uvicorn $(APP) --host $(HOST) --port $(PORT) $(RELOAD) --log-level $(LOG_LEVEL_DEV) --app-dir $(APP_DIR)

prod:
	uvicorn $(APP) --host $(HOST) --port $(PORT) --log-level $(LOG_LEVEL_PROD) --app-dir $(APP_DIR)

ngrok:
	ngrok http $(PORT)