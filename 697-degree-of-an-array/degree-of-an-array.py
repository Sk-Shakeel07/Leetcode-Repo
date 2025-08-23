class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = {}
        count = {}
        degree = 0
        res = float('inf')

        for i, a in enumerate(nums):
            if a not in first:
                first[a] = i
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)

        return res if res != float('inf') else 0
