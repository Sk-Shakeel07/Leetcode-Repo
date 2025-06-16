class Solution {

    private int[][][] dp;

    public int removeBoxes(int[] boxes) {
        int n = boxes.length;
        dp = new int[n][n][n];
        
        // Initialize with -1 to indicate uncomputed states
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    dp[i][j][k] = -1;

        return solve(0, n - 1, 0, boxes);
    }

    private int solve(int l, int r, int k, int[] boxes) {
        if (l > r) return 0;

        if (dp[l][r][k] != -1) return dp[l][r][k];

        int originalL = l, originalK = k;

        // Combine boxes of the same color
        while (l + 1 <= r && boxes[l] == boxes[l + 1]) {
            l++;
            k++;
        }

        // Case 1: Remove boxes[l] and contiguous same-colored boxes
        int ans = (k + 1) * (k + 1) + solve(l + 1, r, 0, boxes);

        // Case 2: Try merging with same colored boxes later
        for (int m = l + 1; m <= r; m++) {
            if (boxes[m] == boxes[l]) {
                ans = Math.max(ans,
                        solve(m, r, k + 1, boxes) + solve(l + 1, m - 1, 0, boxes));
            }
        }

        dp[originalL][r][originalK] = ans;
        return ans;
    }
}
