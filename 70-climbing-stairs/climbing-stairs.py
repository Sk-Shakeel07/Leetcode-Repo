class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

sol = Solution()
print(sol.climbStairs(3))  
print(sol.climbStairs(5))  
'''
Recursive one -->
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
'''