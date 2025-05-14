import math

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        arrowX = -float('inf')
        for point in sorted(points, key=lambda x: x[1]):
            if point[0] > arrowX:
                ans += 1
                arrowX = point[1]
        return ans
