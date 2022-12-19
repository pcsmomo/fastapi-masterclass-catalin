from fastapi import FastAPI
from app.database import models
from app.database.database import engine
from app.routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(post.router)


@app.get('/')
def hw():
    return "Hello world!"


# this will create a database file
models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='app/images'), name='images')

origins = [
    'http://localhost:3000',
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
