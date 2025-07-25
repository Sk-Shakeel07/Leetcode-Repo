class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_island = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_island = max(max_island, dfs(r, c))

        return max_island
