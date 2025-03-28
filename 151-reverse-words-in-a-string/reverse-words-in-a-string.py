class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

sol = Solution()
print(sol.reverseWords("the sky is blue"))      
print(sol.reverseWords("  hello world  "))       
print(sol.reverseWords("a good   example"))      
