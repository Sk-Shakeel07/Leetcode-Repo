class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                current_length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length