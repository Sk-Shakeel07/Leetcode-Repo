class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  # First and last element of each row is 1

            for j in range(1, i):  # Compute the inner values
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)  # Add row to triangle
        
        return triangle

sol = Solution()
print(sol.generate(5))  
print(sol.generate(1))  
