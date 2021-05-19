"""
Binary search tree insertion and search implementation in Python
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(root, key):

    if root is None:
        root = Node(key)
        return root

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    #base cases
    if not root or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


if __name__=='__main__':

    root = insert(None, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)

    print('Inorder Traversal of tree is:', end=' ')
    inorder(root)
    print()

    res = search(root, 60)
    if res:
        print("Node with key found in the tree")
    else:
        print("Key not found in the tree")
        
        
