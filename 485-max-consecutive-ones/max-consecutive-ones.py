class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxi = 0
        for i in nums:
            if i == 0:
                count = 0
            else:
                count += 1
            maxi = max(maxi, count)
        return maxi
