class Solution {
    public boolean checkValidString(String s) {
        int x = 0, y = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                x++;
                y++;
            } else if (ch == ')') {
                x--;
                y--;
            } else { // ch == '*'
                x--;
                y++;
            }

            if (x < 0) x = 0;
            if (y < 0) return false;
        }
        return x == 0;
    }
}
