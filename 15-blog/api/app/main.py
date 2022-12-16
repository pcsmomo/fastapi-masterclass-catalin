from fastapi import FastAPI
from app.database import models
from app.database.database import engine


app = FastAPI()


@app.get('/')
def hw():
    return "Hello world!"


# this will create a database file
models.Base.metadata.create_all(engine)
