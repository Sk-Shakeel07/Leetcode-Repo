class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist between left and right
        curr = prev.next
        next_node = None
        prev_sub = prev

        for _ in range(right - left + 1):
            next_temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = next_temp

        # Connect the reversed part
        prev_sub.next.next = curr
        prev_sub.next = next_node

        return dummy.next
