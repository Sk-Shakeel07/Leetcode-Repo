class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # Target is in left half
                    right = mid - 1
                else:  # Target is in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in right half
                    left = mid + 1
                else:  # Target is in left half
                    right = mid - 1

        return -1


solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  
print(solution.search([4,5,6,7,0,1,2], 3))  
print(solution.search([1], 0))              
