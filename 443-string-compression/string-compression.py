class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        totalIndex, index = 0, 0
        while index < len(chars):
            currChar = chars[index]
            count = 0
            while (index<len(chars) and chars[index] == currChar):
                count +=1
                index +=1
            chars[totalIndex] = currChar
            totalIndex += 1
            if count != 1:
                for c in str(count):
                    chars[totalIndex] = c
                    totalIndex +=1
        chars[:] = chars[:totalIndex]
        return len(chars)