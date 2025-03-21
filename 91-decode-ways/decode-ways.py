class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        prev2, prev1 = 1, 1  # dp[i-2] and dp[i-1]
        
        for i in range(1, len(s)):
            current = 0
            if '1' <= s[i] <= '9':  # Single-digit check
                current += prev1
            if "10" <= s[i-1:i+1] <= "26":  # Two-digit check
                current += prev2
            
            prev2, prev1 = prev1, current
        
        return prev1

sol = Solution()
print(sol.numDecodings("12"))   
print(sol.numDecodings("226"))  
print(sol.numDecodings("06"))  
