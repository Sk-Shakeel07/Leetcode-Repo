import java.util.*;

class Solution {
    static final int N = 1000;
    List<Integer>[] adj = new ArrayList[N];
    Node[] v = new Node[N];
    int timer;

    static class Node {
        int in = 0, out = 0, xorSum = 0;
        Node() {}
    }

    public Solution() {
        for (int i = 0; i < N; i++) {
            adj[i] = new ArrayList<>();
            v[i] = new Node();
        }
    }

    private void dfs(int i, int p, int[] nums) {
        Node node = v[i];
        node.in = timer++;
        node.xorSum = nums[i];
        for (int j : adj[i]) {
            if (j == p) continue;
            dfs(j, i, nums);
            node.xorSum ^= v[j].xorSum;
        }
        node.out = timer++;
    }

    private boolean isAncestor(int anc, int desc) {
        return v[anc].in <= v[desc].in && v[desc].out <= v[anc].out;
    }

    private int score(int x, int y, int z) {
        int[] arr = {x, y, z};
        Arrays.sort(arr);
        return arr[2] - arr[0];
    }

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            adj[i].clear();
            v[i] = new Node();
        }

        for (int[] e : edges) {
            int i = e[0], j = e[1];
            adj[i].add(j);
            adj[j].add(i);
        }

        timer = 0;
        dfs(0, -1, nums);
        int total = v[0].xorSum;
        int ans = Integer.MAX_VALUE;

        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x, y, z;
                int xI = v[i].xorSum, xJ = v[j].xorSum;

                if (isAncestor(i, j)) {
                    x = xJ;
                    y = xI ^ xJ;
                    z = total ^ xI;
                } else if (isAncestor(j, i)) {
                    x = xI;
                    y = xJ ^ xI;
                    z = total ^ xJ;
                } else {
                    x = xI;
                    y = xJ;
                    z = total ^ x ^ y;
                }

                ans = Math.min(ans, score(x, y, z));
            }
        }

        return ans;
    }
}
