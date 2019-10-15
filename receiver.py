# -*- coding: utf-8 -*-

import pika
import time
import logging
#
#Optimize and use a failure on auto_ack or callback 
# Also, cleanup is required + argsparse + commandline args

Q = "PIKA_QUEUE"


#Creating pika connection queue and its params 
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)

def callback(ch, method, properties, body):
	if body:
		for line in body:
		    print("Received message {}\n".format(str(line)))
	print("[x] Done")
	print('Received Data')


#TODO: Add SIGINT to break the script 

channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=True)

# logger.info('Waiting to receive....')
print("Ready to receive message from {} queue.".format(Q))
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
