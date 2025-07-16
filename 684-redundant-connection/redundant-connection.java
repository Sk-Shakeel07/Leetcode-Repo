class Solution {

    class DisjointSet {
        int[] parent;
        int[] size;

        public DisjointSet(int n) {
            parent = new int[n + 1];
            size = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int findUPar(int node) {
            if (parent[node] == node) return node;
            return parent[node] = findUPar(parent[node]); // Path compression
        }

        public void unionBySize(int u, int v) {
            int pu = findUPar(u);
            int pv = findUPar(v);
            if (pu == pv) return;

            if (size[pu] < size[pv]) {
                parent[pu] = pv;
                size[pv] += size[pu];
            } else {
                parent[pv] = pu;
                size[pu] += size[pv];
            }
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        DisjointSet ds = new DisjointSet(n);
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (ds.findUPar(u) == ds.findUPar(v)) {
                return edge;
            } else {
                ds.unionBySize(u, v);
            }
        }
        return new int[0]; // default return if no redundant edge found
    }
}
