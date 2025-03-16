import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s))


sol = Solution()
valid_numbers = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
invalid_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

print("Valid tests:")
for num in valid_numbers:
    print("{}: {}".format(num, sol.isNumber(num)))

print("\nInvalid tests:")
for num in invalid_numbers:
    print("{}: {}".format(num, sol.isNumber(num)))
