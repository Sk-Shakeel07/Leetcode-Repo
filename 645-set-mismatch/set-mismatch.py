class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0] * (n + 1)#count[0] is unused

        for num in nums:
            count[num] += 1

        res = []

        for i in range(1, n + 1):
            if count[i] == 0:
                res.append(i) # Missing number
            elif count[i] == 2:
                res.insert(0, i)# Duplicate number (put first in result)

        return res