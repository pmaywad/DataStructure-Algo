"""
Python implementation of min heap using heapq module
"""

from heapq import heapify, heappop, heappush


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def extract_min(self):
        return heappop(self.heap)

    def decrease_key(self, i, val):
        self.heap[i] = val
        while i != 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])
            i = self.parent(i)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def insert_key(self, val):
        heappush(self.heap, val)

    def get_min(self):
        return self.heap[0]


if __name__=='__main__':
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)

    print(heapObj.extract_min())
    print(heapObj.get_min())
    heapObj.decrease_key(2, 1)
    print(heapObj.get_min())

