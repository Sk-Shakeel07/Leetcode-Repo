class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        for i in range(1, length):
            for j in range(i + 1, length):
                first, second, remaining = num[:i], num[i:j], num[j:]
                if (first.startswith('0') and first != '0') or (second.startswith('0') and second != '0'):
                    continue
                while remaining:
                    third = str(int(first) + int(second))
                    if not remaining.startswith(third):
                        break
                    first = second
                    second = third
                    remaining = remaining[len(third):]
                if not remaining:
                    return True
        return False
