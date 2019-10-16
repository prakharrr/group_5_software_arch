# Group 5 [Software Architecture]
## Members
1. Prakhar Rawat
2. Shimon Johnsom
3. Steven Simmons




### Pre-Requisites:
 1. Install `rabbit-mq` from here https://www.rabbitmq.com/download.html for your OS
 2. Assuming you have python3, Run the rabbit-mq server : `rabbitmq-server` in a separate shell
 3. In separate instances of shell/terminal run:
    * a. `python3 receiver.py`
    * b. `python3 sender.py`

This is the Non-deterministic fault that we've injected in the application
#### CHANGE ME!!!!!
```python
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

```

### Running 

![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/process_all.png "Running instance")

### Architecture
![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/HB.png "Architecture")

### Final Running example
![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/HB.png "Detection of HeartBeat")

