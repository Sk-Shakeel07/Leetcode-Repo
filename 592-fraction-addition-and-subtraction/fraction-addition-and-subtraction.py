import re
from fractions import gcd  # in Python 2, use this from fractions

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        nums = map(int, re.findall(r'[+-]?\d+', expression))
        numerator = 0
        denominator = 1

        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den

        common_divisor = gcd(numerator, denominator)
        return "%d/%d" % (numerator // common_divisor, denominator // common_divisor)
