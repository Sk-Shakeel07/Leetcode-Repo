class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return constructBST(nums, 0, nums.length - 1);
    }

    private TreeNode constructBST(int[] nums, int left, int right) {
        if (left > right) return null; // Base case: return null when the range is invalid

        int mid = left + (right - left) / 2; // Avoid integer overflow
        TreeNode root = new TreeNode(nums[mid]); // Create the root node

        root.left = constructBST(nums, left, mid - 1); // Build left subtree
        root.right = constructBST(nums, mid + 1, right); // Build right subtree

        return root;
    }
}
