
from time import time
import pika


credentials = pika.PlainCredentials('zohreh','zohreh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
ch = connection.channel()
ch.exchange_declare(exchange='topic_logs',exchange_type='topic')
masseges = {
    'error.warning.important':'this is an important massege!',
    'info.debug.notimportant':'this is not an important massege!'
}

for k,v in masseges.item():
    ch.basic_publish(exchange='topic_logs',routing_key=k,body=v,properties=pika.BasicProperties(
    headers={"name":"amir","age":"30"}
    ))
    print("sent!")
    connection.close()
