class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        left, right = 0, 1
        max_len = 1

        while right < len(nums):
            if nums[right] > nums[right - 1]:
                max_len = max(max_len, right - left + 1)
            else:
                left = right
            right += 1
        return max_len
