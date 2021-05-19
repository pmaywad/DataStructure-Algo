"""
Implementation of stack in python using LifoQueue
"""
from queue import LifoQueue

stack = LifoQueue(maxsize=4)

#PUSH operation is done using put() method for queue
stack.put(4)
stack.put(5)
stack.put(6)
stack.put(7)

if stack.full():
    print("Stack is full")
    print("SIZE:", stack.qsize())

#POP operation using get() in LIFO order
for i in range(stack.qsize()):
    print("Popped item is:", stack.get())

if stack.empty():
    print("Stack is empty")
