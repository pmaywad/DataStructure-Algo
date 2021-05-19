"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrder(self, root, level, dic):
        if root is None:
            return
        
        dic.setdefault(level, []).append(root.val)
        self.preOrder(root.left, level+1, dic)
        self.preOrder(root.right, level+1, dic)
        
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = {}
        res = []
        self.preOrder(root, 1, dic)
        for i in range(len(dic)):
            res.append(dic[i+1])
            
        return res

            
