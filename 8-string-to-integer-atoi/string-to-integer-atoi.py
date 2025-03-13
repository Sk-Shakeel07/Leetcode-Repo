class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        
        # Clamp the number to fit within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num


if __name__ == "__main__":
    solution = Solution()
    test_cases = ["42", "   -042", "1337c0d3", "0-1", "words and 987"]
    for s in test_cases:
        print("Input: '{}' -> Output: {}".format(s, solution.myAtoi(s)))
