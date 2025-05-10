class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0, remove remaining k digits from the end of the stack
        if k > 0:
            stack = stack[:-k]

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        # Handle edge case where result might be empty
        return result if result else '0'
