class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x  # Base cases
        
        left, right = 1, x  # Define search range
        ans = 0  # To store the result
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid  # Store potential answer
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        
        return ans  # Return the floored square root
