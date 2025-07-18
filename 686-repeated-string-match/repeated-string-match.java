class Solution {
    public int repeatedStringMatch(String a, String b) {
        int s1 = a.length();
        int s2 = b.length();
        String temp = a;
        int count = 1;

        // Repeat a until b is found in it
        while (!a.contains(b)) {
            a += temp;
            count++;

            // Optimization: If a becomes too long and still doesn't contain b, return -1
            if (a.length() > b.length() + 2 * temp.length()) {
                return -1;
            }
        }

        return count;
    }
}
