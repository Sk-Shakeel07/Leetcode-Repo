class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if(n<=k):
            return null
        res = []
        l, r = 1,n
        while(len(res) != n):
            if(k %2 != 0):
                res.append(l)
                l+=1
            else:
                res.append(r)
                r-=1
            if(k>1):
                k-=1
        return res