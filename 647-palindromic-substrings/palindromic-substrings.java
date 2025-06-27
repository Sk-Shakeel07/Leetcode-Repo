class Solution {
    public int countSubstrings(String s) {
        if(s.length() == 0) return 0;
        int n = s.length();
        int res = 0 ;
        char[] c= s.toCharArray();
        
        for(int i = 0 ; i < n ; i++){
            //Odd and even lengths (Center for odd --> i , i)
            //Center for even --> i , i+1
            res += isPalindrome(i , i , c);
            res += isPalindrome(i, i + 1 , c);
        }
        return res;
    }
    
    public int isPalindrome(int s , int e , char[] c){
        int count = 0;
        while(s >= 0 && e < c.length && c[s--] == c[e++])
            count++;
        
        return count;
    }
}