class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort to handle duplicates efficiently
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                            right -= 1
                    
                    elif total < target:
                        left += 1  # Need a larger sum
                    
                    else:
                        right -= 1  # Need a smaller sum
        
        return result


solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0)) 
print(solution.fourSum([2,2,2,2,2], 8)) 
