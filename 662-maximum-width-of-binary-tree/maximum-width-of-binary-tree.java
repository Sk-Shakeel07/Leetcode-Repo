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
   public int widthOfBinaryTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> qIndex = new LinkedList<>();
        q.add(root);
        qIndex.add(1); //store index, assuming root's index is 1
        int max = 0;
        while(!q.isEmpty())
        {
            int size = q.size();
            int start = 0, end = 0;
            for(int i=0; i<size; i++)
            {
                TreeNode node = q.remove();
                int index = qIndex.remove();
                if(i==0) start = index; //start and end index for each level
                if(i==size-1) end = index;
                if(node.left!=null)
                {
                    q.add(node.left);
                    qIndex.add(2*index);
                }
                
                if(node.right!=null)
                {
                    q.add(node.right);
                    qIndex.add(2*index+1);
                }
            }
            max = Math.max(max, end - start + 1);
        }
        return max;    
    }
}