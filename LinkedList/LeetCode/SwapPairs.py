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
        if head is None or head.next is None:
            return head
        
        temp1 = head
        temp2 = head.next
        prev_node = head
        head = temp2
        while temp1 and temp2:
            prev_node.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1
            prev_node = temp1
            temp1 = temp1.next
            if not temp1:
                break
            temp2 = temp1.next
         
        return head
