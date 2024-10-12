import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.queue_declare(queue="one")
def callback(ch,method,properties,body):
    print(f'we grt your massage:{body}')
    

ch.basic_consume(queue="one",on_message_callback=callback,auto_ack=True)
print("waiting for massage ")
ch.start_consuming()
