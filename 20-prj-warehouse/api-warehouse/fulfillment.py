import time
from redis_om import get_redis_connection
from main import Product

redis = get_redis_connection(
    host="localhost",
    port=6379,
    password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81",
)

key = 'order-completed'
group = 'warehouse-group'

try:
    redis.xgroup_create(name=key, groupname=group, mkstream=True)
    print("Group created")
except Exception as e:
    print(str(e))

try:
    redis.execute_command('auth eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')
except Exception as e:
    print(str(e))

while True:
    try:
        results = redis.xreadgroup(
            groupname=group, consumername=key, streams={key: '>'})
        print(results)
        if results != []:
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj['product_id'])
                    product.quantity -= int(obj['quantity'])
                    product.save()
                except:
                    redis.xadd(name='refund-order', fields=obj)
    except Exception as e:
        print(str(e))
    time.sleep(3)
