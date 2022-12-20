from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from app.routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)


@app.get('/')
def hw():
    return "Hello world!"


models.Base.metadata.create_all(engine)