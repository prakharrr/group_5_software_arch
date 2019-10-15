# -*- coding: utf-8 -*-

import pika
import time
import threading
import logging
#
#Optimize and use a failure on auto_ack or callback 
# Also, cleanup is required + argsparse + commandline args

Q = "PIKA_QUEUE"


#Creating pika connection queue and its params 
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))



channel = conn.channel()

channel.queue_declare(Q)

message_lock = 0

def callback(ch, method, properties, body):
	ticker.cancel()

	if body:
		print("Received message {}\n".format(body))

	print("[x] Done")
	print('Received Data')
	#message_lock = 0
	#lock()
	ticker.start

def lock():
	# ignore if 1, active callback
	print("Fail. No messages coming in")

ticker = threading.Timer(interval=3.0, function=lock)

#TODO: Add SIGINT to break the script 

channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=True)

# logger.info('Waiting to receive....')
ticker.start()
print("Ready to receive message from {} queue.".format(Q))
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()