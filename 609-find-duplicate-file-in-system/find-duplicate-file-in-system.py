from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        h = defaultdict(list)
        while len(paths):
            p = paths.pop()  # pop the item to avoid doubling of memory used.
            parts = p.split()
            folder, files = parts[0], parts[1:]
            for f in files:
                s = f.split('(', 1)  # stops when '(' char is first encountered.
                fn = folder + '/' + s[0]
                content = s[1][:-1]  # remove the trailing ')'
                h[content].append(fn)
        
        ans = []
        for k in h:
            if len(h[k]) > 1:
                ans.append(h[k])
        
        return ans
