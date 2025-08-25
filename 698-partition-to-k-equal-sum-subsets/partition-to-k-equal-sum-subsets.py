class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        n = len(nums)
        memo = {}

        def dfs(used, curr):
            if used == (1 << n) - 1:
                return True
            if (used, curr) in memo:
                return memo[(used, curr)]
            for i in range(n):
                if not (used >> i) & 1 and curr + nums[i] <= target:
                    new_curr = curr + nums[i]
                    nxt = 0 if new_curr == target else new_curr
                    if dfs(used | (1 << i), nxt):
                        memo[(used, curr)] = True
                        return True
            memo[(used, curr)] = False
            return False

        return dfs(0, 0)
