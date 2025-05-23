class Solution {
    
    private int helper(String s, int left, int right, int [][] cache){
        if(left==right)
            return 1;
        
        if(left>right)
            return 0;
        
        if(cache[left][right]!=-1)
            return cache[left][right];
        
        if(s.charAt(left) == s.charAt(right)){
            cache[left][right] = 2 + helper(s, left+1, right-1, cache);
            return cache[left][right];
        }
        
        int leftIncrement = helper(s,left+1,right, cache);
        int rightIncrement =  helper(s,left,right-1, cache);                          
        cache[left][right] = Math.max(leftIncrement, rightIncrement);
        return cache[left][right];
        
        
    }
    
    
    public int longestPalindromeSubseq(String s) {
        /* If the two ends of a string are the same, then they must be included in the longest palindrome subsequence. Otherwise, both ends cannot be included in the longest palindrome subsequence. */
        
        int size = s.length();
        if(size==0 || s==null)
            return 0;
        int [][] dp = new int[size][size];
        for (int[] row : dp) 
            Arrays.fill(row, -1);
        return helper(s, 0, s.length()-1,dp);
    }
}