class ListNode {
    int val;
    ListNode next;
    
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    
    // Method to deserialize a list from an array representation
    public static ListNode deserialize(String data) {
        if (data == null || data.isEmpty()) return null;
        String[] values = data.replace("[", "").replace("]", "").split(",");
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (String val : values) {
            current.next = new ListNode(Integer.parseInt(val.trim()));
            current = current.next;
        }
        return dummy.next;
    }
}

class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode dummy = new ListNode(0);
        ListNode current = head;
        
        while (current != null) {
            ListNode prev = dummy;
            ListNode nextNode = current.next;
            
            while (prev.next != null && prev.next.val < current.val) {
                prev = prev.next;
            }
            
            current.next = prev.next;
            prev.next = current;
            
            current = nextNode;
        }
        
        return dummy.next;
    }

    // Helper method to print the linked list
    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " -> ");
            head = head.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListNode head = ListNode.deserialize("[4,2,1,3]");
        Solution solution = new Solution();
        ListNode sortedHead = solution.insertionSortList(head);
        printList(sortedHead); 
        head = ListNode.deserialize("[-1,5,3,4,0]");
        sortedHead = solution.insertionSortList(head);
        printList(sortedHead); 
    }
}
