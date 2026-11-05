
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import engine
from app.routers.auth_routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Verify database connectivity during application startup.
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("ShopEase Authentication Service started successfully!")
    yield
    engine.dispose()
    print("ShopEase Authentication Service stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    description="Independent JWT Authentication Microservice for ShopEase",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "message": "ShopEase Authentication Service is running",
        "status": "healthy",
    }


@app.get("/health")
def health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }


app.include_router(auth_router)
