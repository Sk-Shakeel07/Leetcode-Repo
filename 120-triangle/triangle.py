class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell with the minimum path sum
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]  # The top element now contains the minimum path sum

solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  
print(solution.minimumTotal([[-10]]))  
