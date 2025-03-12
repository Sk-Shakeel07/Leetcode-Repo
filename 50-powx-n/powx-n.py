class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1  # Base case: x^0 = 1
        
        if n < 0:
            x = 1 / x  # Convert negative power to positive
            n = -n
        
        result = 1
        while n:
            if n % 2:  # If n is odd
                result *= x
            x *= x  # Square the base
            n //= 2  # Reduce exponent by half
        
        return result


sol = Solution()
print(sol.myPow(2.00000, 10))  
print(sol.myPow(2.10000, 3))   
print(sol.myPow(2.00000, -2))  
