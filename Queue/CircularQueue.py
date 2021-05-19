"""
Implementation of Circular Queue in Python
"""


class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.front = self.rare = -1
        self.queue = [None] * self.size


    def enqueue(self, ele):

        #check for full queue
        if (self.rare == self.size - 1 and self.front == 0) or (self.rare == self.front - 1):
            print("Queue is full")
            return
          
        if self.front == -1:
            self.front = 0
            self.rare = 0
        elif self.rare == self.size - 1 and self.front != 0:
            self.rare = 0
        else:
            self.rare += 1
        self.queue[self.rare] = ele

    def dequeue(self):

        #check for empty queue
        if self.front == -1:
            print("Queue is empty")
            return

        val = self.queue[self.front]
        if self.front == self.rare:
            self.front = self.rare = -1

        elif self.front == self.size -1:
            self.front = 0

        else :
            self.front += 1


    def display_queue(self):

        i = self.front
        if self.front == -1:
            print("Queue is empty")

        else:
            while i <= self.rare:
                print(self.queue[i])
                i += 1


if __name__=="__main__":

    queue = CircularQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.display_queue()
    queue.dequeue()
    queue.dequeue()
    print("Front", queue.front)
    print("Rare", queue.rare)
    queue.display_queue()



