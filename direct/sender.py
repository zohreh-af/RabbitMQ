import time
import pika


credentials = pika.PlainCredentials('zohreh','zohreh')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',credentials=credentials))
ch = connection.channel()
ch.queue_declare(queue="one")

ch.basic_publish(exchange='',routing_key="one",body="hello world",properties=pika.BasicProperties(
    # content_type="text/plain",
    # content_encoding="gzip",
    # timestamp=10000000,
    # expiration=str(time.time()),
    # delivery_mode=2,
    # #app_id=11,
    # type="exch.queue",
    headers={"name":"amir","age":"30"}
    ))
print("sent!")
connection.close()