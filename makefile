APP = app.main:app
HOST = 0.0.0.0
PORT = 8000
RELOAD = --reload
LOG_LEVEL_DEV = debug
LOG_LEVEL_PROD = info


dev:
	uvicorn $(APP) --host $(HOST) --port $(PORT) $(RELOAD) --log-level $(LOG_LEVEL_DEV)

prod:
	uvicorn $(APP) --host $(HOST) --port $(PORT) --log-level $(LOG_LEVEL_PROD)

ngrok:
	ngrok http $(PORT)