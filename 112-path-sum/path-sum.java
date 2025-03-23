class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // Base case: If the root is null, return false
        if (root == null) return false;

        // If it's a leaf node and sum matches, return true
        if (root.left == null && root.right == null && targetSum == root.val) {
            return true;
        }

        // Recursively check left and right subtrees with the updated targetSum
        return hasPathSum(root.left, targetSum - root.val) || 
               hasPathSum(root.right, targetSum - root.val);
    }
}
