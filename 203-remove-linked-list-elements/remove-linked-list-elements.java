class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0); // Dummy node before head
        dummy.next = head;
        ListNode current = dummy; // Pointer to traverse the list

        while (current.next != null) {
            if (current.next.val == val) {
                current.next = current.next.next; // Skip the node
            } else {
                current = current.next; // Move to the next node
            }
        }
        
        return dummy.next; // New head
    }
}
