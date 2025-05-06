class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert string to list to allow modification
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("IceCreAm"))   
    print(sol.reverseVowels("leetcode"))   
    print(sol.reverseVowels("hello"))      
    print(sol.reverseVowels("AEIOU"))      
