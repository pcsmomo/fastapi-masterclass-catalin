from fastapi import FastAPI
from app.router import blog_get, blog_post, user
from app.db import models
from app.db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)
