class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # Initialize max sum to negative infinity
        
        def dfs(node):
            if not node:
                return 0  # Base case: return 0 for null nodes
            
            # Recursively calculate max path sum for left and right subtrees
            left_gain = max(dfs(node.left), 0)  
            right_gain = max(dfs(node.right), 0)  
            
            # Calculate the path sum including the current node
            path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum if the new path sum is greater
            self.max_sum = max(self.max_sum, path_sum)
            
            # Return the maximum gain including the current node and one of its children
            return node.val + max(left_gain, right_gain)
        
        dfs(root)  # Start DFS from the root
        return self.max_sum
