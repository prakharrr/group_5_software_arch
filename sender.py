# -*- coding: utf-8 -*-

import pika
from datetime import datetime
import random

import time
TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))


Q="PIKA_QUEUE"

# DEFINE ROUTING KEY FOR SECURITY LATER

# ROUTING_KEY = ""

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)
channel.confirm_delivery()

def failure():
	log = ''
	for i in range(0,10)[::-1]:
		time.sleep(1)
		print('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
		log.join('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
		print("[MONITOR] Sent Data data at -- {}".format(now))
	return(log)


channel.basic_publish(exchange="", routing_key=Q, body=failure(), properties=pika.BasicProperties(delivery_mode=1))

conn.close()
