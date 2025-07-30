class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int maxLen = 0, xMax = 0;

        for (int r = 0, l = 0; r < n; r++) {
            while (r < n && nums[r] == xMax) {
                r++;
            }
            if (r == n || nums[r] < xMax) {
                maxLen = Math.max(maxLen, r - l);
                l = r + 1;
            } else {
                xMax = nums[r];
                maxLen = 1;
                l = r;
            }
        }
        return maxLen;
    }
}
