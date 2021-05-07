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
        if not l1 or not l2: return l2 or l1
        
        if l1.val >= l2.val:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
        
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        last = len(lists)
        if last == 0:
            return None
        
        last = last-1 
        
        # Repeat until only one list is left
        while (last != 0):
            i = 0
            j = last
  
            # (i, j) forms a pair
            while (i < j):
             
                # Merge List i with List j and store
                # merged list in List i
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
  
                # Consider next pair
                i += 1
                j -= 1
             
                # If all pairs are merged, update last
                if (i >= j):
                    last = j
  
        return lists[0]
