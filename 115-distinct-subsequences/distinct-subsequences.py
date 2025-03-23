class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # DP table where dp[i][j] represents the number of distinct subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: An empty string `t` is a subsequence of any `s`
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]

sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))  
print(sol.numDistinct("babgbag", "bag"))     