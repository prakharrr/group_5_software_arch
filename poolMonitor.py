from concurrent.futures import ThreadPoolExecutor
from queue import PriorityQueue
from random import randint
from threading import Thread
import time

fibonacciNum = 33

class PriorityThread(Thread):

    def __init__(self, priority, name):
        Thread.__init__(self)
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return '[' + str(self.priority) + ']: ' + self.name

    def start(self):
        print(self.name + ': Fibonacci')
        print(Fibonacci(fibonacciNum))

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def fib(name):
    # Make task more intensive
    print(name + ': Fibonacci')


if __name__ == '__main__':
    q = PriorityQueue()

    with ThreadPoolExecutor(max_workers = 10) as pool:
        # pool.submit(fib())
        # {executor.submit(load_url, url, 60): url for url in URLS}
        threadArr = []

        for i in range(10):
            threadArr.append(PriorityThread(randint(1,10), 'Thread-' + str(i+1)))
            q.put(threadArr[i])

        for i in range(10):
            print('queue size:', q.qsize())
            print(*q.queue)
            nextThread = q.get()
            print('Popped: ', nextThread)
            nextThread.start()
            #for thread in threadArr:
            #   thread.priority += 1
            newThread = PriorityThread(randint(1, 10), 'Thread-' + str(i + 1))
            threadArr.append(newThread)
            print('Added: ' + str(newThread))
            q.put(newThread)
