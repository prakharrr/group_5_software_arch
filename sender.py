# -*- coding: utf-8 -*-

import pika
from datetime import datetime
import random
import sys
import time
TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))


Q="PIKA_QUEUE"

# DEFINE ROUTING KEY FOR SECURITY LATER

# ROUTING_KEY = ""

# Setting the FileName for the logs
filename = 'logfile'
file = open(filename,'a+')
file.truncate(0)


# Creating connection 
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)

def sender(a,b):
	log = []
	log.append('A/B is {}'.format(a/b))
	mess = 'A={} | B={}'.format(a,b)
	file.write('[SUCCESS] '+ mess + '\n')
	return mess.join(log)

for upper in range(100,10,-1):
	log = []
	up = upper
	lo = random.randint(0,10)
	time.sleep(1)
	try:
		print('[SUCCESS] Numbers are: A={} | B={}'.format(up,lo))
		channel.basic_publish(exchange="", routing_key=Q, body=sender(up,lo), properties=pika.BasicProperties(delivery_mode=1))	
	except:
		log.append('[ERROR] Error detected. Logging A and B to logfile!')
		file.write('[ERROR] Numbers are: A={} | B={} \n'.format(up,lo))
		log = ''.join(log)
		channel.basic_publish(exchange="", routing_key=Q, body=log, properties=pika.BasicProperties(delivery_mode=1))	
		break

conn.close()
