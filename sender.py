# -*- coding: utf-8 -*-

import pika
from datetime import datetime

TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))


Q="PIKA_QUEUE"
# DEFINE ROUTING KEY FOR SECURITY LATER
# ROUTING_KEY = ""

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)

channel.basic_publish(exchange="", routing_key=Q, body="Every Pizza is a personal pizza if you believe in yourself!!!")

print("[MONITOR] Sent Beep boop beeep at -- {}".format(now))

conn.close()
