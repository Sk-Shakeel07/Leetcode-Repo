class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums1:
            if i == nums2[-1]:
                l.append(-1)
            else:
                for j in range(nums2.index(i) + 1, len(nums2)):
                    if nums2[j] > i:
                        l.append(nums2[j])
                        break
                else:
                    l.append(-1)
        return l
