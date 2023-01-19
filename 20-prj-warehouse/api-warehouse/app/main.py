from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import HashModel
from app.config import get_settings
from redis_om import get_redis_connection

config = get_settings()

redis = get_redis_connection(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.post('/product')
def create(product: Product):
    return product.save()


@app.get('/product/{pk}')
def read(pk: str):
    return Product.get(pk)


@app.get('/products')
def all():
    # return Product.all_pks()
    return [format(pk) for pk in Product.all_pks()]


def format(pk: str):
    product = Product.get(pk)
    return {
        'id': pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.delete('/product/{pk}')
def delete(pk: str):
    return Product.delete(pk)
