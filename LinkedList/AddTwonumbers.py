# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        temp1 = l1.next
        temp2 = l2.next
        res = l1.val + l2.val
        carry = 0
        if res > 9:
            l3.val = res%10
            carry = 1
        else:
            l3.val = res
            carry = 0
        prev_node = l3
        while temp1 and temp2:
            node = ListNode()
            res = temp1.val + temp2.val + carry
          
            if res > 9:
                node.val = res % 10
                carry = 1
            else:
                node.val = res
                carry = 0
            prev_node.next = node
            prev_node = node
            temp1 = temp1.next
            temp2 = temp2.next
            
        while temp1:
            node = ListNode()
            res = temp1.val + carry
            if res > 9:
                node.val = res % 10
                carry = 1
            else:
                node.val = res
                carry = 0
            prev_node.next = node
            prev_node = node            
            prev_node.next 
            temp1 = temp1.next
        while temp2:
            node = ListNode()
            node.val = temp2.val
            res = temp2.val + carry
            if res > 9:
                node.val = res % 10
                carry = 1
            else:
                node.val = res
                carry = 0
            prev_node.next = node
            prev_node = node
            temp2 = temp2.next
            
        if carry:
            node = ListNode()
            node.val = carry
            prev_node.next = node
            
        return l3
