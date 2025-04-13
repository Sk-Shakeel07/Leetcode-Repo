class Solution {
    private int dfs(int r,int c,int[][] dp,int[][] matrix,int m,int n)
    {
        if(r<0 || c<0 || r>=m || c>=n) return 0;
        if(dp[r][c]!=-1) return dp[r][c];
        int up=0,down = 0,left =0,right = 0;

        if(r>0 && matrix[r-1][c]> matrix[r][c]) up = 1 + dfs(r-1,c,dp,matrix,m,n);
        if(r<m-1 && matrix[r+1][c]> matrix[r][c]) down = 1 + dfs(r+1,c,dp,matrix,m,n);
        if(c>0 && matrix[r][c-1]> matrix[r][c]) left = 1 + dfs(r,c-1,dp,matrix,m,n);
        if(c<n-1 && matrix[r][c+1]> matrix[r][c]) right = 1 + dfs(r,c+1,dp,matrix,m,n);
        return  dp[r][c] = Math.max(Math.max(up,down),Math.max(left,right));

    }
    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int ans = Integer.MIN_VALUE;

        int[][] dp = new int[m][n];
        for(int[] row:dp) Arrays.fill(row,-1);

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                int val = 1 + dfs(i,j,dp,matrix,m,n);
                ans = Math.max(ans,val);
            }
        }
        return ans;
    }
}