"""
Inorder traversal of binary tree without recursion

1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inorder(root):

    if not root:
        return None
    stack = []
    current = root
    while True:
        while current:
            stack.append(current)
            current = current.left
        temp = stack.pop()
        print(temp.data, end=' ')
        current = temp.right
        if not current and len(stack) == 0:
            break


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
