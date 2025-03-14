# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Create a dummy node before the head
        dummy.next = head
        first = second = dummy

        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next  # Return the new head
