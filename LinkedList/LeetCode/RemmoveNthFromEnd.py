# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def lenght(self, head):
        lenght = 0
        temp = head
        while temp:
            lenght += 1
            temp = temp.next
        return lenght
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenght = self.lenght(head)
        lenght = lenght - n + 1
        temp = head
        prev = None
        while temp:
            lenght -= 1
            if lenght == 0:
                break
            prev = temp
            temp = temp.next
        if prev:
            prev.next = temp.next
        if prev == None:
          if temp.next:
            head = temp.next
          else:
            head = None
        
        return head
