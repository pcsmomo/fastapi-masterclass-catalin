from fastapi import FastAPI
from app.router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}
