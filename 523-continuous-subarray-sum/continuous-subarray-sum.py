class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_cache = {0: -1}
        remainder = 0
        for i in xrange(len(nums)):
            remainder += nums[i]
            if k != 0:
                remainder %= k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >= 2:
                return True
        return False
