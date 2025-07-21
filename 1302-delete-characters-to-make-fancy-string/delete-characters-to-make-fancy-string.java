class Solution {
    public String makeFancyString(String s) {
        StringBuilder str = new StringBuilder();
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i > 1 && count == 2 && s.charAt(i) == s.charAt(i - 1)) {
                continue;
            }

            str.append(s.charAt(i));

            if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1;
            }
        }

        return str.toString();
    }
}
