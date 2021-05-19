"""
Depth First Traversal for binary tree in Python
"""


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

def preorder(root):

    if not root:
        return None

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print('Inorder Traversal of tree is:', end=' ')
    inorder(root)
    print('\nPreorder Traversal of tree is:',end=' ')
    preorder(root)
    print('\nPostorder Traversal of tree is:', end=' ')
    postorder(root)

    
