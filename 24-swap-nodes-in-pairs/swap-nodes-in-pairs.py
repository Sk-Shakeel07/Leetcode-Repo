class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next
