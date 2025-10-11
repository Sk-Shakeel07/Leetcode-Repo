from random import randint

class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        blacklist = set(blacklist)  # avoid TLE
        self.N = n - len(blacklist)  # to be used in pick()
        key = [x for x in blacklist if x < n - len(blacklist)]
        val = [x for x in range(n - len(blacklist), n) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self):
        """
        :rtype: int
        """
        i = randint(0, self.N - 1)
        return self.mapping.get(i, i)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
