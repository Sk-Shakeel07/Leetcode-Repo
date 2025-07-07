class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        dp_l = [1] * n  # Length of LIS ending at index i
        dp_f = [1] * n  # Count of LIS ending at index i

        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_l[j] + 1 > dp_l[i]:
                        dp_l[i] = dp_l[j] + 1
                        dp_f[i] = dp_f[j]
                    elif dp_l[j] + 1 == dp_l[i]:
                        dp_f[i] += dp_f[j]
            max_len = max(max_len, dp_l[i])

        res = 0
        for i in range(n):
            if dp_l[i] == max_len:
                res += dp_f[i]

        return res
