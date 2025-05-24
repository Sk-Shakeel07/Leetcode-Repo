import java.util.regex.Pattern;

class Solution {
    public boolean detectCapitalUse(String word) {
        return Pattern.matches("([A-Z]+|[a-z]+|[A-Z][a-z]*)", word);
    }
}