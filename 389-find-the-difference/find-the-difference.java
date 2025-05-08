class Solution {
    public char findTheDifference(String s, String t) {
        char[] tArr = t.toCharArray();  // Convert string t to a character array
        for (int i = 0; i < s.length(); i++) {
            tArr[i + 1] += tArr[i] - s.charAt(i);  // Propagate the difference
        }
        return tArr[tArr.length - 1];  // The final character holds the answer
    }
}