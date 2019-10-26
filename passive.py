# -*- coding: utf-8 -*-

import pika
from datetime import datetime
import random
import sys

import time
TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))
print('Using Pika version: %s' % pika.__version__)
Q="PIKA_QUEUE"

# DEFINE ROUTING KEY FOR SECURITY LATER

# ROUTING_KEY = ""

# File for logging
filename = 'logfile'
file = open(filename,'r+')
# file.truncate(0)

err_val = 0

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)



def passive(a,b):
	log = []
	log.append('[SUCCESS] A/B is {}'.format(a/b))
	mess = 'A={} | B={}'.format(a,b)
	return mess.join(log)

def restart(err_val):
	"""
	calls method with the failed value
	"""
	print('Received last known value: {}'.format(err_val))
	print('\n ***[MONITOR] Starting Passive Service with last checkpoint {}*** \n'.format(err_val))

	for upper in range(int(err_val),1,-1):
		log = []
		up = upper
		lo = random.randint(1,10)
		time.sleep(1)
		try:
			print('[SUCCESS] Numbers are: A={} | B={}'.format(up,lo))
			channel.basic_publish(exchange="", routing_key=Q, body=passive(up,lo), properties=pika.BasicProperties(delivery_mode=1))	
		except:
			# log.append('[ERROR] Error detected. Logging A and B to logfile!')
			# file.write('[ERROR] Numbers are: A={} | B={} \n'.format(up,lo))
			# log = ''.join(log)
			print('[MONITOR] Problem in Passive Service. Exiting now!')
			sys.exit(1)
			# channel.basic_publish(exchange="", routing_key=Q, body=log, properties=pika.BasicProperties(delivery_mode=1))

isAlive=True
while isAlive:
	where = file.tell()
	line = file.readline()
	if not line:
		time.sleep(1)
		file.seek(where)
	elif '[ERROR]' in line:
		isAlive = False
		err_val = line.strip()[23:25]
		print(err_val)
		restart(err_val)
conn.close()
