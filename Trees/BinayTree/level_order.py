
"""
Level order traversal of binary tree in Python
"""

from queue import Queue

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def levelOrderTraversal(root):

    if root == None:
        return

    queue = Queue()

    temp = root
    while temp:
        print(temp.data, end=' ')
        if temp.left:
            queue.put(temp.left)
        if temp.right:
            queue.put(temp.right)

        temp = queue.get()

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    levelOrderTraversal(root)
