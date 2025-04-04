class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, path, total):
            # If we've picked k numbers
            if len(path) == k:
                if total == n:
                    result.append(list(path))
                return

            for i in range(start, 10):  # Only digits 1 through 9
                if total + i > n:
                    break  # Prune the branch
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return result
