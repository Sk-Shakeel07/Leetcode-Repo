class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        counter = Counter(s)  # Count of each character
        stack = []
        in_stack = set()

        for char in s:
            counter[char] -= 1
            if char in in_stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)
