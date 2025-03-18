class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        count = 1  # At least one partition is needed
        
        for char in s:
            if char in seen:  # If duplicate, start new partition
                count += 1
                seen.clear()
            seen.add(char)
        
        return count


sol = Solution()
print(sol.partitionString("abacaba"))  
print(sol.partitionString("ssssss"))   
