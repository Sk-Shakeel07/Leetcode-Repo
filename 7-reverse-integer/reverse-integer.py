class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        negative = x < 0
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
           
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return -reversed_num if negative else reversed_num


sol = Solution()
print(sol.reverse(123)) 
print(sol.reverse(-123)) 
print(sol.reverse(120)) 
print(sol.reverse(0))    
