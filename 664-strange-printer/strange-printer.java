class Solution {
     public int strangePrinter(String s) {
        int[][] mt = new int[s.length()][s.length()];

        for (int i = s.length() - 1 ; i >= 0; i--) {
            for (int j = 0; j < s.length(); j++) {
                if (i > j) continue;
                if (i == j) {
                    mt[i][j] = 1;
                    continue;
                }

                mt[i][j] = Integer.MAX_VALUE;

                for (int k = i; k < j; k++) {
                    mt[i][j] = Math.min(mt[i][j], mt[i][k] + mt[k + 1][j]);
                }

                if (s.charAt(i) == s.charAt(j)) mt[i][j]--;
            }
        }

        return mt[0][s.length() - 1];
    }
}