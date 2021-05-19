"""
Implementation of Queue in python using queue.Queue()
"""

from queue import Queue

queue = Queue(maxsize=3)
queue.put(10)
queue.put(5)
queue.put(6)

#Check is queue is full
print("Queue full?", queue.full())
#dequeuing queue using get() method
print("Dequeued element from queue is:", queue.get())
print("Dequeued element from queue is:", queue.get())
print("Dequeued element from queue is:", queue.get())
#check for empty queue
print("Queue empty?", queue.empty())
