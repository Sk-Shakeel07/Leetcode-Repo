class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* that can match an empty string
        for j in range(2, n + 1, 2):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # '*' means zero occurrences of preceding element
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]  # '*' means one or more occurrences

        return dp[m][n]


sol = Solution()
print(sol.isMatch("aa", "a"))     
print(sol.isMatch("aa", "a*"))    
print(sol.isMatch("ab", ".*"))    
print(sol.isMatch("mississippi", "mis*is*p*."))  
print(sol.isMatch("mississippi", "mis*is*ip*.")) 
