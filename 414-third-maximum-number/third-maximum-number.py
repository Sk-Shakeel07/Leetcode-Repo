class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sorted(set(nums), reverse=True)
        if len(res) >= 3:
            return res[2]
        else:
            return res[0]