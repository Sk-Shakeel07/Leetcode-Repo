class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, n = 0, len(nums)
        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total