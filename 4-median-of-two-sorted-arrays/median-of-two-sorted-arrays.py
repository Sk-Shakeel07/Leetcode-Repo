class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):  # Ensure nums1 is the smaller array
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left_half_size = (m + n + 1) // 2
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = left_half_size - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1


solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))       
print(solution.findMedianSortedArrays([1, 2], [3, 4]))    
