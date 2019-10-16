# -*- coding: utf-8 -*-

import sys
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

# Monitoring components

def callback(ch, method, properties, body):
	message_lock = 1

	if body:
		print("Received message {}\n".format(body))

	print("[x] Done")
	print('Received Data')
	message_lock = 0
	last_updated = time.time() # update last received message time

def lock():
	while True:

		# If at least 5s before last update and no messages
		if (time.time() - last_updated) >= 5 & message_lock == 0:
			print("Fail. No messages coming in")
			sys.exit(1)

# Monitor components
last_updated = time.time()
message_lock = 0
monitor = threading.Thread(name='monitor', target=lock, args='')

#TODO: Add SIGINT to break the script 

channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=True)

# logger.info('Waiting to receive....')
monitor.start()
last_updated = time.time() # reset time just in case
print("Ready to receive message from {} queue.".format(Q))
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()