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

def failure():
	log = []
	for i in range(10):
		time.sleep(2)
		log.append('[FAULTY_MODULE] Working for ' + str(i) + ' seconds.\n')
		print("[MONITOR] Sent transmission data at -- {}".format(now))
		print(('[FAULTY_MODULE] Working for ' + str(i) + ' seconds.'))
	return (str(log))

channel.basic_publish(exchange="", routing_key=Q, body=failure())


conn.close()

