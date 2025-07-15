public class Solution {
    public boolean isValid(String s) {
        if (s.length() < 3) return false;

        int vowels = 0, consonants = 0;

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                if ("aeiouAEIOU".indexOf(c) >= 0) {
                    vowels++;
                } else {
                    consonants++;
                }
            } else if (!Character.isDigit(c)) {
                // Not a letter or digit
                return false;
            }
        }

        return vowels >= 1 && consonants >= 1;
    }
}
