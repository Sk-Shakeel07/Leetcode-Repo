class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])


sol = Solution()
print(sol.lengthOfLastWord("Hello World")) 
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  
print(sol.lengthOfLastWord("luffy is still joyboy")) 
