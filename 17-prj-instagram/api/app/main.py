from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import models
from app.db.database import engine
from app.routers import user, post, comment
from app.auth import authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)


@app.get('/')
def hw():
    return "Hello world!"


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='app/images'), name='images')
