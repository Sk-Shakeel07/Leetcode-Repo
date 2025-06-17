class Solution 
{
    int MOD = (int)(1e9 + 7);
    public int checkRecord(int n) 
    {
        long[][] dp = new long[n+1][3];
        dp[0][0] = dp[0][1] = dp[0][2] = 1; 
        dp[1][0] = 1;  
        dp[1][1] = 1;   
        dp[1][2] = dp[1][0] + dp[1][1];
        for (int i = 2; i <= n; i++)
        {
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD;
            dp[i][1] = (dp[i-1][0] + dp[i-2][0]) % MOD;
            dp[i][2] = dp[i][0] + dp[i][1];
        }        
        long res = dp[n][2];      
        for (int i = 0; i < n; i++) 
        {
            long temp = (dp[i][2] * dp[n-1-i][2]) % MOD; 
            res = (res + temp) % MOD; 
        }     
        return (int)res;
    }
} 