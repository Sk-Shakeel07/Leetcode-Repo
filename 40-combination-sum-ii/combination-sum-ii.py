class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))  # Found a valid combination
                return
            if target < 0:
                return  # Stop recursion if target becomes negative
            
            for i in range(start, len(candidates)):
                # Skip duplicates (Only allow the first occurrence in a recursion level)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])  # Choose the current number
                backtrack(i + 1, target - candidates[i], path)  # Move to the next index
                path.pop()  # Backtrack
        
        backtrack(0, target, [])
        return result

'''
Differences Between the Two Problems
Feature 	         Combination Sum (Unlimited Use)	        Combination Sum II(SingleUse)
Can reuse numbers?	✅ Yes, a number can be used multiple times.	❌ No, each number can be used only once.
Handles duplicates?	❌ No need, since all numbers are distinct.	✅ Yes, must remove duplicate sets.
Sorting required?	❌ Not necessary.	               ✅ Sorting helps in skipping duplicates.
Recursive call index Call with i to allow reuse.	Call with i + 1 to avoid reuse.
'''
