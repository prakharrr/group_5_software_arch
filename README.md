# Group 5 [Software Architecture]
## Members
1. Prakhar Rawat
2. Shimon Johnsom
3. Steven Simmons

https://github.com/prakharrr/group_5_software_arch/.github/workflows/CI/badge.svg

### Pre-Requisites:
 1. Install `rabbit-mq` from here https://www.rabbitmq.com/download.html for your OS
 2. Assuming you have python3, Run the rabbit-mq server : `rabbitmq-server` in a separate shell
 3. In another shell just type: `python3 receiver.py`
 4. Type `make` in another shell

#### Fault in sender

```python
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
```

### Running 

![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/process_all.png "Running instance")

### Architecture
![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/HB.png "Architecture")

### Final Running example
![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/HB.png "Detection of HeartBeat")

