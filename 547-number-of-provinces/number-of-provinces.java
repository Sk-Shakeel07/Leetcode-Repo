import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                // Choose either DFS or BFS:
                dfs(i, isConnected, visited);    // \U0001f501 Depth-First Search
                // bfs(i, isConnected, visited); // \U0001f501 Breadth-First Search
                count++;
            }
        }
        return count;
    }

    // Depth-First Search (Recursive)
    private void dfs(int node, int[][] isConnected, boolean[] visited) {
        visited[node] = true;
        for (int j = 0; j < isConnected.length; j++) {
            if (isConnected[node][j] == 1 && !visited[j]) {
                dfs(j, isConnected, visited);
            }
        }
    }

    // Breadth-First Search (Using Queue)
    private void bfs(int start, int[][] isConnected, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int j = 0; j < isConnected.length; j++) {
                if (isConnected[node][j] == 1 && !visited[j]) {
                    visited[j] = true;
                    queue.offer(j);
                }
            }
        }
    }
}
