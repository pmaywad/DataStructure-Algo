"""
Implementation of Queue using Stacks in Python
"""


class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, ele):
        #Push x to stack1
        self.stack1.append(ele)

    def dequeue(self):
        #If both stacks are empty then display queue is empty
        if not self.stack1 and not self.stack2:
            print("Queue is empty")
            return

        #If stack2 is empty, while stack1 is not empty, push everything from stack1 to stack2.
        n = len(self.stack1)
        if not self.stack2:
            while n > 0:
                self.stack2.append(self.stack1.pop())
                n -= 1

        return self.stack2.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

