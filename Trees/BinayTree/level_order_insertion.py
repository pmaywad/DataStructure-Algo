"""
Insertion in binary tree in level order in Python
"""

from queue import Queue

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inorder(root):

    if not root:
        return None
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


def insert(root, key):

    if not root:
        return

    queue = Queue()

    temp = root
    while temp:

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            queue.put(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            queue.put(temp.right)

        temp = queue.get()

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    print("Inorder before insertion", end=' ')
    inorder(root)
    insert(root, 7)
    print()
    print("Inorder after insertion", end=' ')
    inorder(root)



