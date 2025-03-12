class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to handle duplicates
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                        right -= 1
                
                elif total < 0:
                    left += 1  # Move left pointer to get a larger sum
                
                else:
                    right -= 1  # Move right pointer to get a smaller sum
                    
        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4])) 
print(solution.threeSum([0, 1, 1])) 
print(solution.threeSum([0, 0, 0]))  
