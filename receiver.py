# -*- coding: utf-8 -*-

import pika
import time
from datetime import datetime
import multiprocessing
import logging
import sys
from pika.compat import unicode_type, dictkeys, is_integer
TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))
#
#Optimize and use a failure on auto_ack or callback 
# Also, cleanup is required + argsparse + commandline args

Q = "PIKA_QUEUE"


#Creating pika connection queue and its params 
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)


def callback(ch, method, properties, body):

	# time.sleep(5)
	body = body.decode('utf-8')
	for line in (body.split(',')):
		if 'Result' in line:
		    print ('Received data: {}'.format(line))
		elif 'ERROR' in line:
			print('[*] Error detected in the sender at -- {}'.format(now))
			print('[MONITOR] An error has been detected at the sender\'s end. \nPlease check the system and run again')
			# sys.exit(1)
	print("Received: delivery tag: {0}\tchannel num: {1}".format(method.delivery_tag, ch.channel_number))

print("Ready to receive message from {} queue.".format(Q))
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=True)

channel.start_consuming()
