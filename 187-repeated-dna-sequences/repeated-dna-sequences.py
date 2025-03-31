class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):  # Iterate through all 10-letter substrings
            sequence = s[i:i+10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        
        return list(repeated)

if __name__ == "__main__":
    sol = Solution()
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s2 = "AAAAAAAAAAAAA"

    print(sol.findRepeatedDnaSequences(s1))  
    print(sol.findRepeatedDnaSequences(s2)) 
