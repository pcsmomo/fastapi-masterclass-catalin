from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from redis_om import HashModel
import requests
import time
from app.redis.services import redis
from app.config import get_settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

config = get_settings()


class ProductOrder(HashModel):
    product_id: str
    quantity: int

    class Meta:
        database = redis


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str

    class Meta:
        database = redis


@app.post("/orders")
def create(productOrder: ProductOrder, background_tasks: BackgroundTasks):
    req = requests.get(
        f'http://{config.WAREHOUSE_HOST}:{config.WAREHOUSE_PORT}/product/{productOrder.product_id}')
    product = req.json()
    fee = product['price'] * 0.2

    order = Order(
        product_id=productOrder.product_id,
        price=product['price'],
        fee=fee,
        total=product['price'] + fee,
        quantity=productOrder.quantity,
        status='pending'
    )

    order.save()

    # order_complete(order)
    background_tasks.add_task(order_complete, order)

    return order


@app.get('/orders/{pk}')
def get(pk: str):
    return format(pk)


@app.get('/orders')
def get_all():
    return [format(pk) for pk in Order.all_pks()]


def format(pk: str):
    # order = Order(pk=pk)
    # order.load()
    order = Order.get(pk)
    return {
        'id': order.pk,
        'product_id': order.product_id,
        'price': order.price,
        'fee': order.fee,
        'total': order.total,
        'quantity': order.quantity,
        'status': order.status
    }


def order_complete(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
