class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))  # Found a valid combination
                return
            if target < 0:
                return  # Stop if target becomes negative
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # Choose a number
                backtrack(i, target - candidates[i], path)  # Continue with reduced target
                path.pop()  # Backtrack
        
        backtrack(0, target, [])
        return result
