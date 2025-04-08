class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) / 2  # or use // if using Python 2.2+
        return int(total - sum(nums))
