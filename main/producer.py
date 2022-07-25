import pika, json

# RabbitMQ
params = pika.URLParameters("amqps://yeojlxzv:6VgzN2g7BTUAEimlDB7mRFfv56VqARJi@mustang.rmq.cloudamqp.com/yeojlxzv")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
