from fastapi import FastAPI
from app.database import models
from app.database.database import engine
from app.routers import post
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(post.router)


@app.get('/')
def hw():
    return "Hello world!"


# this will create a database file
models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='app/images'), name='images')
