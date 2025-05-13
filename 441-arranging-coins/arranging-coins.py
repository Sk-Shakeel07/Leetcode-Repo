class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 0, n
        while L <= R:
            M = (L + R) // 2
            if M * (M + 1) // 2 <= n:
                L = M + 1
            else:
                R = M - 1
        return R
