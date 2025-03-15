class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):  # Iterate from right to left
            curr_value = roman_values[char]
            if curr_value < prev_value:
                total -= curr_value  # Subtraction case
            else:
                total += curr_value  # Normal addition case
            prev_value = curr_value  # Update previous value for next iteration
        
        return total


solution = Solution()
print(solution.romanToInt("III"))     
print(solution.romanToInt("LVIII"))   
print(solution.romanToInt("MCMXCIV")) 
