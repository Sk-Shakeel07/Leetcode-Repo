class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null; // Empty list, return null
        
        return buildTree(head, null);
    }

    private TreeNode buildTree(ListNode head, ListNode tail) {
        if (head == tail) return null; // Base case: when head reaches tail

        ListNode mid = findMiddle(head, tail); // Find middle node
        TreeNode root = new TreeNode(mid.val); // Create the root node

        root.left = buildTree(head, mid);     // Left subtree
        root.right = buildTree(mid.next, tail); // Right subtree

        return root;
    }

    private ListNode findMiddle(ListNode head, ListNode tail) {
        ListNode slow = head, fast = head;
        while (fast != tail && fast.next != tail) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow; // Middle node
    }
}
