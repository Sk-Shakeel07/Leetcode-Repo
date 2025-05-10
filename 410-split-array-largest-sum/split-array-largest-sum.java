class Solution {
    public int splitArray(int[] nums, int k) {
        int low = 0, high = 0;

        for (int num : nums) {
            high += num;
            low = Math.max(low, num);
        }

        int ans = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canSplit(nums, k, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }

    private boolean canSplit(int[] nums, int k, int maxSum) {
        int count = 1;
        int currentSum = 0;

        for (int num : nums) {
            if (currentSum + num <= maxSum) {
                currentSum += num;
            } else {
                count++;
                currentSum = num;
            }
        }

        return count <= k;
    }
}
