from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        t_count = Counter(t)  # Frequency of characters in t
        window_count = {}  # Frequency of characters in the current window
        required_chars = len(t_count)  # Number of unique characters needed
        formed_chars = 0  # Number of unique characters matched

        left = 0
        min_len = float("inf")
        min_window = ""

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # If the current character matches the required frequency
            if char in t_count and window_count[char] == t_count[char]:
                formed_chars += 1

            # Try to minimize the window while keeping all required characters
            while formed_chars == required_chars:
                # Update minimum window substring
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                # Shrink the window from the left
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    formed_chars -= 1
                
                left += 1  # Move left pointer

        return min_window

sol = Solution()
print sol.minWindow("ADOBECODEBANC", "ABC") 
print sol.minWindow("a", "a")               
print sol.minWindow("a", "aa")              
print sol.minWindow("abc", "ac")            
print sol.minWindow("ABFCAB", "ABC")        
