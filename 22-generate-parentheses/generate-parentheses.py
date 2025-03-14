class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)
        return result


sol = Solution()
print(sol.generateParenthesis(3))  
print(sol.generateParenthesis(1))  
