class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in reversed(range(32)):
            answer <<= 1
            prefixes = set([num >> i for num in nums])
            temp = answer | 1
            found = False
            for p in prefixes:
                if temp ^ p in prefixes:
                    found = True
                    break
            if found:
                answer |= 1
        return answer
