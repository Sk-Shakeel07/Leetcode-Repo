class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k > n, take modulo to optimize

        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    sol = Solution()
    sol.rotate(nums1, k1)
    print(nums1)  

    nums2 = [-1, -100, 3, 99]
    k2 = 2
    sol.rotate(nums2, k2)
    print(nums2) 
