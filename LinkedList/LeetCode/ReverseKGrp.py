# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        node1 = node2
        return node1
    
    def lenght(self, head):
        if not head:
            return 0
        lenght = 0
        temp = head
        while temp:
            lenght += 1
            temp = temp.next
        return temp
            
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lenght = self.lenght(head)
