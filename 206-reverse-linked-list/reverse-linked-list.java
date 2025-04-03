class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode nextNode = current.next; // Store next node
            current.next = prev;  // Reverse the link
            prev = current;       // Move prev to current node
            current = nextNode;   // Move to next node
        }
        
        return prev; // New head of the reversed list
    }
}
