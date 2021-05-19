"""
Implementation of stack in python using deque
"""
from collections import deque

stack = deque()

#PUSH operatio using append()
stack.append(4)
stack.append(5)
stack.append(6)

print("Stack is", stack)

#POP operation using pop() in LIFO order
for i in range(len(stack)):
    print("Popped item is:", stack.pop())
    
    
