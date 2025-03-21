from fastapi import FastAPI

from api.routers import models
from api.config.db import create_db_and_tables


app = FastAPI()


app.include_router(models.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World!"}
