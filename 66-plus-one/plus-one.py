class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        for i in range(n - 1, -1, -1):  # Traverse from the last digit to the first
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Return early if no carry-over is needed
            digits[i] = 0  # Set current digit to 0 if it's 9 (carry over)

        # If we exit the loop, it means all digits were 9, so we need an extra 1 at the start
        return [1] + digits  

solution = Solution()
print(solution.plusOne([1, 2, 3]))  
print(solution.plusOne([4, 3, 2, 1])) 
print(solution.plusOne([9]))  
print(solution.plusOne([9, 9, 9]))  
