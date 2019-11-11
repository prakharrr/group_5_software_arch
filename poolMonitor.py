from concurrent.futures import ThreadPoolExecutor
from queue import PriorityQueue
from random import randint
from threading import Thread
import time

class PriorityThread(Thread):

    def __init__(self, priority, name):
        Thread.__init__(self)
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return self.name + ": " +  str(self.priority)

    def start(self):
        fib()

def fib():
    print("Fibonacci")

if __name__ == '__main__':
    q = PriorityQueue()

    with ThreadPoolExecutor(max_workers = 10) as pool:
        # pool.submit(fib())
        # {executor.submit(load_url, url, 60): url for url in URLS}
        threadArr = []

        for i in range(10):
            threadArr.append(Thread(name='Thread-', target=fib, args=''))
            q.put(PriorityThread(i+1, 'Thread-' + str(i+1)))

        #print(threadArr.__len__())
        #q.put({7, threading.Thread(name='monitor', target=fib, args='')})
        #q.put({5, threading.Thread(name='monitor', target=fib, args='')})
        #q.put({10, threading.Thread(name='monitor', target=fib, args='')})


        while q.qsize() > 0:
            print('queue size:', q.qsize())
            print(*q.queue)
            print('Popped: ', q.get())
            time.sleep(1)

