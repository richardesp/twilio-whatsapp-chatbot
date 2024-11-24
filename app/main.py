from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn.config
from routes.whatsapp import router as whatsapp_router

# Initialize FastAPI
app = FastAPI()

# Include routers
app.include_router(whatsapp_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
