import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
# 因為這個.py檔是在djagon project外面，所以import db model時要先設定好django
from products.models import Product

# RabbitMQ
params = pika.URLParameters("amqps://yeojlxzv:6VgzN2g7BTUAEimlDB7mRFfv56VqARJi@mustang.rmq.cloudamqp.com/yeojlxzv")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print("Product likes increased")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()