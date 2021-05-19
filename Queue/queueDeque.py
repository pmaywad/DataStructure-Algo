"""
Implementation of Queue in python using deque
"""

from collections import deque

queue = deque()
queue.append(10)
queue.append(5)
queue.append(6)

print("Queue is ", queue)
#dequeue first element
print("Popped item is:", queue.popleft())

print("Remaining queue is:", queue)
