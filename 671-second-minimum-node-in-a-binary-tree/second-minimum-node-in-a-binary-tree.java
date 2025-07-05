/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int rootVal;
    private long ans;
    
    public int findSecondMinimumValue(TreeNode root) {
        // Initialize the smallest value and answer
        rootVal = root.val;
        ans = Long.MAX_VALUE;
        
        // Traverse the tree to find the second minimum
        dfs(root);
        
        // If ans was never updated, return -1
        return (ans == Long.MAX_VALUE) ? -1 : (int) ans;
    }
    
    private void dfs(TreeNode node) {
        if (node == null) return;
        
        // If we find a value strictly between rootVal and current ans, update ans
        if (node.val > rootVal && node.val < ans) {
            ans = node.val;
        }
        // If this node equals the minimum, we need to explore its children
        else if (node.val == rootVal) {
            dfs(node.left);
            dfs(node.right);
        }
    }
}
