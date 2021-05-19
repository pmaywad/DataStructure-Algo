# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return swapPairsRecursive(head)
        
        

def swapSpecificNode(prev, current):
    prev.next = current.next
    current.next = prev
    prev = current

    return prev


def swapPairsRecursive(node):
    if not node or not node.next:
        return node 
    node = swapSpecificNode(node, node.next)
    node.next.next = swapPairsRecursive(node.next.next)
    return node
