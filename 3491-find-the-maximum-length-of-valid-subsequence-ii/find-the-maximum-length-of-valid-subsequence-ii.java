import java.util.*;

class Solution {
    public int maximumLength(int[] nums, int k) {
        // Let dp[i] denote length for subsequence modulo k
        short ans = 0;
        short[] dp = new short[k];

        for (int i = 0; i < k; i++) {
            Arrays.fill(dp, (short) 0);
            for (int x : nums) {
                int j = x % k;
                dp[j] = (short) Math.max(dp[(i + k - j) % k] + 1, dp[j]);
                ans = (short) Math.max(ans, dp[j]);
            }
        }

        return ans;
    }
}
