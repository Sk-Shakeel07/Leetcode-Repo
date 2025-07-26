import java.util.*;

class Solution {
    public long maxSubarrays(int n, int[][] conflictingPairs) {
        List<List<Integer>> pairs = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            pairs.add(new ArrayList<>());
        }

        for (int[] p : conflictingPairs) {
            int s = p[0], e = p[1];
            if (s > e) {
                int temp = s;
                s = e;
                e = temp;
            }
            pairs.get(s).add(e);
        }

        long curr = 0;
        long[] res = new long[n + 2];

        int j = conflictingPairs.length - 1;
        int[] nextEnd = new int[]{n + 1, n + 1};

        for (int i = n; i > 0; i--) {
            for (int end : pairs.get(i)) {
                if (end <= nextEnd[0]) {
                    nextEnd[1] = nextEnd[0];
                    nextEnd[0] = end;
                } else if (end < nextEnd[1]) {
                    nextEnd[1] = end;
                }
                j--;
            }

            curr += nextEnd[0] - i;
            res[nextEnd[0]] += nextEnd[1] - nextEnd[0];
        }

        long maxExtra = 0;
        for (long val : res) {
            maxExtra = Math.max(maxExtra, val);
        }

        return curr + maxExtra;
    }
}
