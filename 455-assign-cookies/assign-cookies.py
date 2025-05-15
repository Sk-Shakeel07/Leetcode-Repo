class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n1 = len(g)
        n2 = len(s)
        count = 0 
        i = 0 
        j = 0 

        while i < n1 and j < n2:
            if g[i] <= s[j]:
                count += 1
                j += 1
                i += 1
            else:
                j += 1
        return count
