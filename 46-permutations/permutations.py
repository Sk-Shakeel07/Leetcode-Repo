class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Append a copy of nums
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)  # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (Undo swap)
        
        backtrack(0)
        return result

sol = Solution()
print(sol.permute([1,2,3]))
