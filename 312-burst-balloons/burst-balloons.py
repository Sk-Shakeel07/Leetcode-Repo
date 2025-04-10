class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Add 1 before and after to simplify edge balloon handling
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create DP table
        dp = [[0] * n for _ in range(n)]
        
        # Build up from smaller subarrays to larger ones
        for length in range(2, n):  # length is the distance between left and right
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        
        return dp[0][n - 1]
