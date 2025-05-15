from collections import Counter

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = Counter()
        for a in nums1:
            for b in nums2:
                count[a + b] += 1

        res = 0
        for c in nums3:
            for d in nums4:
                res += count.get(-(c + d), 0)

        return res
