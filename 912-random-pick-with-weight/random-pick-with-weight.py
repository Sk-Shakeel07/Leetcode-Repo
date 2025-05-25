import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr = [0] * len(w)
        self.arr[0] = w[0]
        for i in range(1, len(self.arr)):
            self.arr[i] = self.arr[i-1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        r = random.randint(1, self.arr[-1])
        idx = bisect.bisect_left(self.arr, r)
        return idx
        