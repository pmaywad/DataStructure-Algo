"""
Binary search tree deletion implementation in Python
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


def min(root):
    temp = root
    while temp.left:
        temp = temp.left
    return temp


def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        else:
            temp = min(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)
    return root


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
    delete(root, 60)
    print('Inorder Traversal of tree is:', end=' ')
    inorder(root)

