class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Base case: if the string is too short to contain any valid substring
        if len(s) < k:
            return 0
        
        # Count the frequency of each character in the string
        for c in set(s):
            if s.count(c) < k:
                # c is a bad character — split the string around it and process each part
                return max(self.longestSubstring(t, k) for t in s.split(c))
        
        # All characters appear at least k times
        return len(s)
