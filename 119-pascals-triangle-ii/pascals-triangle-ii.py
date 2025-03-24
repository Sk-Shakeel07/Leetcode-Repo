class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)  # Initialize the row with 1s
        
        for i in range(1, rowIndex):  # Iterate to update values in-place
            for j in range(i, 0, -1):  # Update from right to left
                row[j] += row[j - 1]
        
        return row

sol = Solution()
print(sol.getRow(3))  
print(sol.getRow(0))  
print(sol.getRow(1))  
