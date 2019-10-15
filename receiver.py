# -*- coding: utf-8 -*-

import pika
import time
import multiprocessing
import logging
import sys
#
#Optimize and use a failure on auto_ack or callback 
# Also, cleanup is required + argsparse + commandline args

Q = "PIKA_QUEUE"


#Creating pika connection queue and its params 
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)


def callback(ch, method, properties, body):

	for line in body:
		if not line:
			ch.basic_ack(delivery_tag = method.delivery_tag)
			print('NACK')
		else:
			ch.basic_nack(delivery_tag = method.delivery_tag) 
			print('ACK')
	print("delivery tag: {0}\tchannel num: {1}\tReceived body: {2}".format(method.delivery_tag, ch.channel_number,\
	body.decode()))
	ch.basic_ack(delivery_tag=method.delivery_tag)


print("Ready to receive message from {} queue.".format(Q))
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(on_message_callback=callback,queue=Q, auto_ack=False)

channel.start_consuming()