class Solution {

    class Pair{
        int zeroes;
        int ones;

        Pair(int zeroes,int ones){
            this.zeroes=zeroes;
            this.ones=ones;
        }
    }
    public int findMaxForm(String[] strs, int m, int n) {
        int k=strs.length;
        Pair[] arr = new Pair[k];
        int[][][] dp = new int[k+1][m+1][n+1];
        for(int i=0;i<k;i++){
            int ones=0,zeroes=0;
            for(int j=0;j<strs[i].length();j++){
                if(strs[i].charAt(j)=='0'){
                    zeroes++;
                }
                else{
                    ones++;
                }
            }

            arr[i]=new Pair(zeroes,ones);
        }
        for(int[][] d2:dp){
            for(int[] d1:d2){
                Arrays.fill(d1,-1);
            }
        }
        return solve(arr,0,m,n,dp);

    }

    public int solve(Pair[] arr,int i,int m ,int n,int[][][] dp){
        if(i>=arr.length){
            return 0;
        }
        if(dp[i][m][n]!=-1){
            return dp[i][m][n];
        }
        int max=0;
        if(m>=arr[i].zeroes&&n>=arr[i].ones){
            max=Math.max(max,1+solve(arr,i+1,m-arr[i].zeroes,n-arr[i].ones,dp));
        }

        max=Math.max(max,solve(arr,i+1,m,n,dp));
        return dp[i][m][n]=max; 
    }
}