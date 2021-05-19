"""
Red-black tree insertion implementation in python
"""

RED = 0
BLACK = 1

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.colour = RED
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNIL = Node(0)
        self.TNIL.colour = BLACK
        self.root = self.TNIL

    def insert(self, key):
        node = Node(key)
        node.colour = RED
        node.left = self.TNIL
        node.right = self.TNIL
        temp = self.root
        y = None
        while temp != self.TNIL:
            y = temp
            if key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = y
        if not y:
            self.root = node
        elif key < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.colour = BLACK
            return

        if node.parent.parent is None:
            return

        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.colour is RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                #CASE 1
                if uncle.colour is RED:
                    node.parent.colour = BLACK
                    uncle.colour = BLACK
                    node.parent.parent = RED
                    node = node.parent.parent
                #CASE 2
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    #CASE 3
                    node.parent.colour = BLACK
                    node.parent.parent.colour = RED
                    self.right_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.left
                #CASE 1
                if uncle.colour is RED:
                    node.parent.colour = BLACK
                    uncle.colour = BLACK
                    node.parent.parent = RED
                    node = node.parent.parent
                #CASE 2
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    #CASE 3
                    node.parent.colour = BLACK
                    node.parent.parent.colour = RED
                    self.left_rotate(node.parent.parent)

        self.root.colour = BLACK

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.TNIL:
            y.left.parent = node
        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node.parent.left == node:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        x = node.left
        node.left = x.right
        if x.right != self.TNIL:
            x.right.parent = node
        x.parent = node.parent
        if not node.parent:
            self.root = x
        elif node.parent.left == node:
            node.parent.left = x
        else:
            node.parent.right = x
        x.right = node
        node.parent = x

    def inorder(self, node):
        if node != self.TNIL:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)



if __name__=='__main__':
    rb_tree = RedBlackTree()
    l = [7, 6, 5, 4, 3, 2, 1]
    for i in l:
        rb_tree.insert(i)
    print("Inorder of tree is:", end=' ')
    rb_tree.inorder(rb_tree.root)


