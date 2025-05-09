class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        int sum = 0, f = 0;
        for(int i = 0; i < n; i++) {
            sum += nums[i];
            f += i * nums[i];
        }
        int max = f;
        for(int i = n - 1; i > 0; i--) {
            f = f + sum - n * nums[i];
            max = Math.max(max, f);
        }
        return max;
    }
}