# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length_and_last(self, head):
        temp = None
        if not head:
            return 0
        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next
        return length, temp
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length, last = self.length_and_last(head)
        k = k%length
        if k == 0:
            return head
        
        temp = head
        
        for i in range(length-k):
            prev_node = temp
            temp = temp.next
        prev_node.next = None   
        prev_head = head
        head = temp
        last.next = prev_head
        return head
