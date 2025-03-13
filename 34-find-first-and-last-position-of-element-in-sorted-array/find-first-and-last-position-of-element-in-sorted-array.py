class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Search on the left side
                    else:
                        left = mid + 1  # Search on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        first = findBound(True)
        last = findBound(False)

        return [first, last]


sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  
print(sol.searchRange([5,7,7,8,8,10], 6))  
print(sol.searchRange([], 0)) 
