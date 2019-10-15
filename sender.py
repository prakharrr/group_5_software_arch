import pika
from datetime import datetime
from random import randint
from time import sleep

TIME_FORMAT = ("%m/%d/%Y %H:%M:%S")
now = (datetime.now().strftime(TIME_FORMAT))
numerator = randint(0, 100)
denominator = randint(0,10)

Q="PIKA_QUEUE"
# DEFINE ROUTING KEY FOR SECURITY LATER
# ROUTING_KEY = ""

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare(Q)

while True:
    if denominator == 0:
        print("I fail now")
    numerator / denominator
    channel.basic_publish(exchange="", routing_key=Q,  body="Every Pizza is a personal pizza if you believe in yourself!!!")
    print("[MONITOR] Sent Beep boop beeep at -- {}".format(now))
    numerator = randint(0, 100)
    denominator = randint(0, 10)
    sleep(1)

conn.close()