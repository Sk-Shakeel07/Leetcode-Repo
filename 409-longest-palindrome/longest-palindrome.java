class Solution {
  public int longestPalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<>();      
        int palindromeSize = 0;
        for(int i =0 ; i<s.length();i++){
            int keyCount = map.getOrDefault(s.charAt(i),0);           
            map.put(s.charAt(i),++keyCount);          
            if (keyCount%2 == 0) palindromeSize +=2;           
        }             
        for (int size : map.values()){
            if (size%2==1){
                palindromeSize++;
                break;
            }
        }
        return palindromeSize;
    }
}