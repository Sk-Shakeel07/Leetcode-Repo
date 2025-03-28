class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:  # Minimum must be in right half
                left = mid + 1
            elif nums[mid] < nums[right]:  # Minimum is in left half (including mid)
                right = mid
            else:  # nums[mid] == nums[right], reduce search space
                right -= 1  

        return nums[left]  # The minimum element
