class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Append a copy of the current subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])   # Include the current element
                backtrack(i + 1, path) # Recur for the next elements
                path.pop()             # Exclude the current element (backtrack)
        
        backtrack(0, [])
        return result


sol = Solution()
print(sol.subsets([1,2,3]))  

