from itertools import izip_longest

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(izip_longest(pattern, s))))
