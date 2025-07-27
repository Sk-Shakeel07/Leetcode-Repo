class Solution {
    public int countHillValley(int[] nums) {
        int n = nums.length;
        int cnt = 0;
        boolean[] diff = new boolean[2]; // diff[0] = false, diff[1] = false

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] == nums[i]) continue;
            boolean bigger = nums[i] > nums[i - 1];
            diff[bigger ? 1 : 0] = true;
            if (diff[0] && diff[1]) {
                cnt++;
                diff[bigger ? 0 : 1] = false;
            }
        }

        return cnt;
    }
}
