class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in range(2**n)]


sol = Solution()
print(sol.grayCode(2))  
print(sol.grayCode(1))  
