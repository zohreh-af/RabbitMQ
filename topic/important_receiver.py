import pika


credentials = pika.PlainCredentials('zohreh','zohreh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='topic_logs',exchange_type='topic')
result = ch.queue_declare(queue="",exclusive=True)
ch.queue_bind(exchange='topic',queue=result.method.queue,routing_key='#.important')
print("waiting for logs...")
print(result.method.queue)

def callback(ch,method,properties,body):
    print(f'we grt your massage:{body}')
    with open("error_log.log",'a') as el:
        el.write(f'{str({body})}\n')
        
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue=result.method.queue,on_message_callback=callback)
print("waiting for massage ")
ch.start_consuming()
