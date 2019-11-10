from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from filecmp import cmp
from queue import Queue, PriorityQueue
from random import randint
import threading
import time

fibonaci = 0

class PriorityTask(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    def __lt__(self, other):
        return self.priority < other.priority

def fib():
    print("Fibonacci")

def main():
    with ProcessPoolExecutor(max_workers=3) as pool:
        pool.submit(fib)


if __name__ == '__main__':
    jobs = []
    print("Hello")

    q = PriorityQueue()

    with ThreadPoolExecutor(max_workers = 10) as pool:
        # pool.submit(fib())
        # {executor.submit(load_url, url, 60): url for url in URLS}
        threadArr = []

        for i in range(10):
            threadArr.append(threading.Thread(name='Thread-', target=fib, args=''))
            q.put(PriorityTask(i, 'Yes'))
            print(randint(1, 10))

        print(threadArr.__len__())
        #q.put({7, threading.Thread(name='monitor', target=fib, args='')})
        #q.put({5, threading.Thread(name='monitor', target=fib, args='')})
        #q.put({10, threading.Thread(name='monitor', target=fib, args='')})


        print('Not dead yet')
        while q.qsize() > 0:
            print('queue size:', q.qsize())
            print(q.queue)
            print(q.get())
            time.sleep(1)

