class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 2  # Allow at most two occurrences, so start from index 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:  # Only place if it's not the same as two places before
                nums[j] = nums[i]
                j += 1
        return j
