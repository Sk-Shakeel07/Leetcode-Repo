class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = {0:-1}
        res = 0
        cur = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                cur -= 1
            else:
                cur += 1
            
            if cur in first:
                res = max(res, idx - first[cur])
            else:
                first[cur] = idx

        return res