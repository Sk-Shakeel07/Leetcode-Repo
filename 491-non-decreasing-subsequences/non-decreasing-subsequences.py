class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        def backtrack(index, path):
            if len(path) >= 2:
                result.add(tuple(path))
            for i in range(index, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return [list(x) for x in result]