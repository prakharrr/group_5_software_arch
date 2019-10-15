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
def failure():
    log = []
    for i in range(5):
        time.sleep(1)
        log.append('[FAULTY_MODULE] Working for ' + str(i) + ' seconds.\n')
        print("[MONITOR] Sent transmission data at -- {}".format(now))
        print(('[FAULTY_MODULE] Working for ' + str(i) + ' seconds.'))
    return (str(log))

```


![alt text](https://github.com/prakharrr/group_5_software_arch/blob/master/assets/PROJECT_HEART.png "Running instance")
