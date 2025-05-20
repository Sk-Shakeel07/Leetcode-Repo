class Solution {
    public int findTargetSumWays(final int[] nums, final int target) {
        final int n = nums.length;

        final int[][] memo = new int[n][2001];

        for(final int[] a : memo)
            Arrays.fill(a, Integer.MAX_VALUE);

        return helper(nums, target, 0, 0, memo);
    }

    private int helper(final int[] nums, final int target, final int idx, final int sum, final int[][] memo) {
        if(idx >= nums.length)
            return sum == target ? 1 : 0;

        if(memo[idx][sum + 1000] != Integer.MAX_VALUE)
            return memo[idx][sum + 1000];

        final int result = helper(nums, target, idx + 1, sum + nums[idx], memo) + helper(nums, target, idx + 1, sum - nums[idx], memo);

        memo[idx][sum + 1000] = result;

        return result;
    }
}