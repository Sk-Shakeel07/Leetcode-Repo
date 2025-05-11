import java.util.*;

class Solution {
    public int strongPasswordChecker(String password) {
        int n = password.length();
        int res = 0, shortLen = 0, extraLen = 0;
        int missingChars = 3;

        if (n < 6) shortLen = 6 - n;

        boolean hasDigit = true, hasUpper = true, hasLower = true;

        for (char ch : password.toCharArray()) {
            if (Character.isDigit(ch) && hasDigit) {
                missingChars--;
                hasDigit = false;
            }
            if (Character.isUpperCase(ch) && hasUpper) {
                missingChars--;
                hasUpper = false;
            }
            if (Character.isLowerCase(ch) && hasLower) {
                missingChars--;
                hasLower = false;
            }
            if (missingChars == 0) break;
        }

        if (n > 20) extraLen = n - 20;

        PriorityQueue<int[]> minQueue = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        int j = 0;
        for (int i = 1; i <= n; i++) {
            if (i == n || password.charAt(i) != password.charAt(j)) {
                int len = i - j;
                if (len >= 3) {
                    minQueue.add(new int[]{len % 3, len});
                }
                j = i;
            }
        }

        int len = extraLen;
        while (!minQueue.isEmpty() && len > 0) {
            int[] top = minQueue.poll();
            int newLen = top[1] - 1;
            len--;
            if (newLen >= 3) {
                minQueue.add(new int[]{newLen % 3, newLen});
            }
        }

        PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());
        while (!minQueue.isEmpty()) {
            maxQueue.add(minQueue.poll()[1]);
        }

        int replaces = 0;
        while (!maxQueue.isEmpty() && maxQueue.peek() >= 3) {
            int curr = maxQueue.poll();
            curr -= 3;
            if (curr >= 3) {
                maxQueue.add(curr);
            }
            replaces++;
        }

        res = extraLen + Math.max(replaces, Math.max(shortLen, missingChars));
        return res;
    }
}
