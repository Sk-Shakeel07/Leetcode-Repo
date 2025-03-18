class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Do not increment mid here

nums1 = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums1)
print(nums1)  

nums2 = [2, 0, 1]
Solution().sortColors(nums2)
print(nums2)  
