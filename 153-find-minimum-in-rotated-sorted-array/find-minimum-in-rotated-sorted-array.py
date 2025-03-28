class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if nums[mid]>=nums[l]:
                if nums[mid]<=nums[r]:
                    return nums[l]
                else:
                    l=mid+1
            else:
                r = mid
        return l