"""
Implementation of Open Addressing in Hashing in Python
"""


class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [None]*self.size

    def hash_function(self, key):
        return key%self.size

    def insert(self, key):
        idx = self.hash_function(key)
        while idx < self.size:
            if self.hash_table[idx] in (None, 'DELETED'):
                self.hash_table[idx] = key
                return
            idx += 1

        print("Hash Table is full")

    def display(self):
        print(self.hash_table)

    def remove(self, key):
        idx = self.hash_function(key)
        while idx < self.size:
            if self.hash_table[idx] == key:
                self.hash_table[idx] = 'DELETED'
                return
            idx += 1

    def search(self, key):
        idx = self.hash_function(key)
        while idx < self.size:
            if self.hash_table[idx] == key:
                return idx
            idx += 1

        return -1


if __name__=='__main__':

    hash_table = HashTable(7)
    hash_table.insert(15)
    hash_table.insert(11)
    hash_table.insert(27)
    hash_table.insert(8)
    hash_table.insert(12)
    hash_table.display()
    hash_table.remove(12)
    hash_table.display()
    idx = hash_table.search(8)
    if idx == -1:
        print("key not found in hash table")
    else:
        print("key found at location", idx)
