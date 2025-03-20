class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check if current node has duplicates
            while current.next and current.val == current.next.val:
                current = current.next  # Move to the last duplicate
            
            # If prev.next is still current, no duplicates were found
            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next  # Skip all duplicates
            
            current = current.next  # Move to the next node
        
        return dummy.next
