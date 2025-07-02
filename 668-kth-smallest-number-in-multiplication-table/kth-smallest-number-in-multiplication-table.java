class Solution {
    // counts number of integers less than or equal to x in multiplication table
    private int count(int m, int n, int x) {
        int ans = 0;
        for (int i = 1; i <= m; i++) {
            ans += Math.min(x / i, n);
        }
        return ans;
    }

    public int findKthNumber(int m, int n, int k) {
        int L = 1, R = m * n, ans = 0;

        while (L <= R) {
            int mid = L + (R - L) / 2;
            if (count(m, n, mid) < k) {
                L = mid + 1;
            } else {
                ans = mid;
                R = mid - 1;
            }
        }
        return ans;
    }
}
