class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = max(nums)
        if M <= 0:
            return M
        else:
            return sum(x for x in set(nums) if x > 0)
