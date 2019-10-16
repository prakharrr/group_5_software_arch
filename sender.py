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


def not_failure():
	"""
	Data which doesn't result in errors at the receiver
	"""
	isAlive=True
	log = []
	err_log = []
	try:
		for i in range(2,10)[::-1]:
			time.sleep(1)
			print('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
			log.append('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
			print("[MONITOR] Sent Data data at -- {}".format(now))
	except:
		isAlive=False
		print('[MONITOR] Problem detected in the sender -- {}'.format(now))
		print('[MONITOR] Could not send the result to receiver -- {}'.format(now))
		err_log.append('[ERROR] Error detected in the sender.')
	return str(log) if isAlive else str(err_log)

def failure():
	"""
	Data which does result in errors at the receiver
	"""
	isAlive=True
	log = []
	err_log = []
	try:
		for i in range(1,10)[::-1]:
			time.sleep(1)
			print('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
			log.append('Result is {}/{}= {}'.format(i,i-1,i//(i-1)))
			print("[MONITOR] Sent Data data at -- {}".format(now))
	except:
		isAlive=False
		print('[MONITOR] Problem detected in the sender -- {}'.format(now))
		print('[MONITOR] Could not send the result to receiver -- {}'.format(now))
		err_log.append('[ERROR] Error detected in the sender.')
	return str(log) if isAlive else str(err_log)

channel.basic_publish(exchange="", routing_key=Q, body=failure(), properties=pika.BasicProperties(delivery_mode=1))
channel.basic_publish(exchange="", routing_key=Q, body=not_failure(), properties=pika.BasicProperties(delivery_mode=1))
# channel.basic_publish(exchange="", routing_key=Q, body=failure(), properties=pika.BasicProperties(delivery_mode=1))

conn.close()
