class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"

        isNegative = num < 0

        num = abs(num)
        quotient = num
        digit = ""

        while quotient != 0:
            digit += str( num % 7 )
            num //= 7
            quotient = num
        
        if isNegative: return "-" + digit[::-1]

        return digit[::-1]