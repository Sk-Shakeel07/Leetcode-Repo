class Solution:
   def isPalindrome(self, s):
        cleaned = ""
        for char in s:
            if char.isalnum():  
                cleaned += char.lower()

        return cleaned == cleaned[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  
print(sol.isPalindrome("race a car"))  
print(sol.isPalindrome(" ")) 
