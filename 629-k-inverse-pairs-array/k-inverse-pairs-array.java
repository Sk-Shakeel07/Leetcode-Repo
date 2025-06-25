class Solution {
    public static int kInversePairs(int n, int k) {
        final int MOD = 1000_000_007;
        int maxPair = n*(n - 1)/2;
        if(k > maxPair) return 0;
        if(k == 0 || k == maxPair) return 1;
        if(k == 1 || k == maxPair - 1) return n - 1;
        int [] dp = new int[4];
        dp[0] = 1;dp[1] = 1;// initialize n =2, [1,1,0,0]; length is the same as maxPair when n = 3 for ease of boundary checking.
        for(int i = 3;i <= n;i++){
            int currMaxPair = i*(i - 1)/2;
            int nextLevelMaxPair = (i+1)*i/2;//to deal with boundary
            int len = i<n? Math.min(nextLevelMaxPair + 1,k + 1) : Math.min(currMaxPair + 1,k + 1);//if it is last loop, no need to expand space for next loop
            int[] currDp = new int[len];
            currDp[0] = 1;//to deal with boundary
            for(int j = 1;j < Math.min(currMaxPair + 1,k + 1);j++){
                if(j < i)
                    currDp[j] = (currDp[j - 1] + dp[j]) % MOD;
                else
                    currDp[j] = (currDp[j - 1] + dp[j] - dp[j - i]) % MOD;
                if(currDp[j] < 0)
                    currDp[j] += MOD;//deal with negative value after %1000_000_007
            }
            dp = currDp;
        }
        return dp[k];
     }
}