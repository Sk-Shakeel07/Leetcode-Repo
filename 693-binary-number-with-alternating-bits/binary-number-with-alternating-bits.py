class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]  # The first 2 characters are always '0b', so we slice them off.
        for i in range(1, len(binary)):
            if binary[i] == binary[i-1]:
                return False
        return True
