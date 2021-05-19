"""
Binary search tree insertion and search implementation in Python
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        temp = self.root
        y = None
        while temp:
            y = temp
            if key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        if not y:
            self.root = node
        elif key < y.data:
            y.left = node
        else:
            y.right = node

    def search(self, key):
        if not self.root:
            print("Tree is empty")
            return -1
        temp = self.root
        while temp and temp.data!=key:
            if key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        if not temp:
            print("Key not found in tree")
            return -1
        else:
            return temp


def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


if __name__=='__main__':

    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print('Inorder Traversal of tree is:', end=' ')
    inorder(bst.root)
    res = bst.search(60)
    if res != -1:
        print("\nNode with key found in tree")

