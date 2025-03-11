class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  # Negative numbers are not palindromes

        reversed_num = 0
        original = x  # Store the original number

        while x > 0:
            digit = x % 10  # Extract the last digit
            reversed_num = reversed_num * 10 + digit  # Append the digit to reversed_num
            x //= 10  # Remove the last digit

        return original == reversed_num  # Check if reversed number is the same as the original

# Example test cases
solution = Solution()
print(solution.isPalindrome(121))   # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))    # Output: False
print(solution.isPalindrome(1221))  # Output: True
