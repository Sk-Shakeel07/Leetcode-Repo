class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0

        # Step 1: Precompute Palindrome Substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or is_palindrome[left + 1][right - 1]):
                    is_palindrome[left][right] = True

        # Step 2: Compute Minimum Cuts using DP
        dp = [float('inf')] * n  # dp[i] = min cuts for s[0:i+1]
        for i in range(n):
            if is_palindrome[0][i]:  # If s[0:i+1] is already a palindrome, no cut needed
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:  # If s[j+1:i+1] is a palindrome
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

sol = Solution()
print(sol.minCut("aab"))  
print(sol.minCut("a"))    
print(sol.minCut("ab"))   
