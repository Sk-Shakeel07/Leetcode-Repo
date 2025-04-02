class Solution(object):
    def get_next(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1

sol = Solution()
print(sol.isHappy(19)) 
print(sol.isHappy(2))   
