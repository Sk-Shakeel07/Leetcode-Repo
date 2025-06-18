class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        num = int(n)
        cands = set([str(10**(length-1)-1), str(10**length+1)])
        prefixLen = (length + 1) // 2
        prefix = int(n[:prefixLen])
        
        for delta in (-1, 0, 1):
            pref = str(prefix + delta)
            if len(pref) > 0:
                if length % 2:
                    cand = pref + pref[:-1][::-1]
                else:
                    cand = pref + pref[::-1]
                cands.add(cand)

        if n in cands:
            cands.remove(n)
        
        best = None
        for cand in cands:
            val = int(cand)
            diff = abs(val - num)
            if best is None or diff < best[0] or (diff == best[0] and val < best[1]):
                best = (diff, val)
        
        return str(best[1])
