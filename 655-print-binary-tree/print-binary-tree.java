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
    List<List<String>> res = new ArrayList<>();
    public List<List<String>> printTree(TreeNode root) {
        int rows = getHeight(root);
        int cols = (int) Math.pow(2, rows) - 1;
        for(int i = 0 ; i < rows; i++) {
            res.add(new ArrayList<>());
            for(int j = 0; j < cols; j++) {
                res.get(i).add("");
            }
        }
        printTree(root, 0, 0, cols - 1);
        return res;
    }
    
    private void printTree(TreeNode root, int row, int left, int right) {
        if(root == null) return;
        int col = (left + right) / 2;
        res.get(row).set(col, root.val + "");
        printTree(root.left, row + 1, left, col - 1);
        printTree(root.right, row + 1, col + 1, right);
    }
    
    private int getHeight(TreeNode root) {
        if(root == null) return 0;
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
        
    }
}