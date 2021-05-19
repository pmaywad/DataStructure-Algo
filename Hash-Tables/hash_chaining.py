"""
Implementation of Hashing with chaining in Python
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, new_data):
        node = Node(new_data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next

        return -1

    def delete(self, key):
        node = self.search(key)
        if node == -1:
            print("Node does not exist")
            return -1
        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev


    def display(self):
        temp = self.head
        while temp:
            print("-->", end='')
            print(temp.data, end='')
            temp = temp.next


class Hash:

    def __init__(self, size):
        self.size = size
        self.hash_table = [None]*self.size

    def hash_function(self, key):
        return key%self.size

    def insert(self, key):
        idx = self.hash_function(key)
        if self.hash_table[idx] is None:
            self.hash_table[idx] = LinkedList()
        self.hash_table[idx].insert(key)

    def display(self):
        for i in range(self.size):
            print(i, end='')
            if self.hash_table[i]:
                self.hash_table[i].display()
            print("\n")

    def remove(self, key):
        idx = self.hash_function(key)
        self.hash_table[idx].delete(key)



if __name__=='__main__':

    hash_table = Hash(7)
    hash_table.insert(15)
    hash_table.insert(11)
    hash_table.insert(27)
    hash_table.insert(8)
    hash_table.insert(12)
    hash_table.display()
    hash_table.remove(12)
    hash_table.display()
