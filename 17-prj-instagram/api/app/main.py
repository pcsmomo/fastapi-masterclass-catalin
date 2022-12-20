from fastapi import FastAPI
from app.db import models
from app.db.database import engine

app = FastAPI()


@app.get('/')
def hw():
    return "Hello world!"


models.Base.metadata.create_all(engine)
