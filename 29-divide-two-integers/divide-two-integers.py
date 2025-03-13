class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define 32-bit integer limits
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # To avoid exceeding 32-bit range

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)  # True if one is negative

        # Convert dividend and divisor to positive values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        # Keep subtracting divisor from dividend while possible
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double temp until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Ensure result is within 32-bit range
        return max(min(quotient, INT_MAX), INT_MIN)


solution = Solution()
print(solution.divide(10, 3))  
print(solution.divide(7, -3))   
