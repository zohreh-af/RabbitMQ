
from time import time
import pika


credentials = pika.PlainCredentials('zohreh','zohreh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
ch = connection.channel()
ch.exchange_declare(exchange='logs',exchange_type='fanout')
ch.basic_publish(exchange='logs',routing_key="",body="hello world",properties=pika.BasicProperties(
    headers={"name":"amir","age":"30"}
    ))
print("sent!")
connection.close()