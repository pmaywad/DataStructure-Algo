class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        memo = {}
        start_idx = 0
        res = 0
        for idx, c in enumerate(s):
            
            if c in memo:
                start_idx = max(memo[c] + 1, start_idx)
            memo[c] = idx
            res = max(idx - start_idx + 1, res)
            
        return res
  
