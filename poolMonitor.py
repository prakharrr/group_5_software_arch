from concurrent.futures import ThreadPoolExecutor
from queue import PriorityQueue
from random import randint
from threading import Thread
import time

fibonacciNum = 33
currPriority = 1

class PriorityThread(Thread):

    def __init__(self, priority, name, number):
        Thread.__init__(self)
        self.priority = priority
        self.name = name
        self.number = number

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return '[' + str(self.priority) + ']: ' + self.name

    def start(self):
        while(currPriority > self.priority):
            pass # Wait
        print(str(self) + ' has started')
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

def IncreaseQueuePriority(queue, priorityIncrease):
    # Increase the priority of each thread in the queue by the given amount
    for thread in q.queue:
        if thread.priority > 1:
            thread.priority -= 1


if __name__ == '__main__':
    q = PriorityQueue()

    with ThreadPoolExecutor(max_workers = 10) as pool:
        # Add 10 threads with random priority into the queue
        for i in range(10):
            q.put(PriorityThread(priority= randint(1,10), name= 'Thread-' + str(i+1), number= i))

        # Loop for 10 additions so doesn't run forever
        for i in range(10):
            # Display threads in queue
            print('queue size:', q.qsize())
            print(*q.queue)

            # Get next thread based on priority
            nextThread = q.get()
            num = nextThread.number # For next thread which will take previous thread's number
            print('Popped: ', nextThread)
            currPriority = nextThread.priority
            print("Current Priority now " + str(nextThread.priority))
            nextThread.start()

            # Increase queue priority for remaining threads
            IncreaseQueuePriority(q, 1)

            # Add another thread to replace the completed thread
            newThread = PriorityThread(randint(1, 10), 'Thread-' + str(i + 1), num)
            q.put(newThread)
            print('Added: ' + str(newThread))
