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
print('Using Pika version: %s' % pika.__version__)


#Creating pika connection queue and its params
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)


def callback(ch, method, properties, body):
	"""
	callback method to check the alive status of the critical process/sender
	"""
	print(str(body))
	body = body.decode('utf-8')
	while not body:
		print('Waiting Waiting ... ... ... ')
	for line in (body.split(',')):
		if 'SUCCESS' in line:
			print('Logging Received data: {}'.format(line))
		elif 'ERROR' in line:
			print('[ERROR] Error detected in the sender at -- {}\n'.format(now))
			print('[MONITOR] Sleeping for 5 seconds to restart passive service\n\n')
			time.sleep(5)
			print('[MONITOR] Waiting for Passive service !')

print("Listening on {} queue.".format(Q))
channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=True)

channel.start_consuming()