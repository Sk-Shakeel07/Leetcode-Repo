class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        s = s.replace(' ', '')
        
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    # Integer division truncating toward zero
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)
                sign = char
                num = 0
        
        return sum(stack)
