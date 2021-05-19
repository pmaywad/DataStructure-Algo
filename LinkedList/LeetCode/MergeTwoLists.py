# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        l3 = ListNode()
        temp3 = l3

        while True:
            if temp1 is None:
                temp3.next = temp2
                break
            if temp2 is None:
                temp3.next = temp1
                break
            node = ListNode()
            temp3.next = node
            temp3 = temp3.next
            if temp1.val < temp2.val:

                node.val = temp1.val
                prev_node = temp1
                temp1 = temp1.next    
            else:

                node.val = temp2.val
                prev_node = temp2
                temp2 = temp2.next

        return l3.next
                
