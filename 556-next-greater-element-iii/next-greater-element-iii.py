class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
            
        if i == 0: return -1
        
        j = i
        while j+1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))
        
        return ret if ret < 1<<31 else -1