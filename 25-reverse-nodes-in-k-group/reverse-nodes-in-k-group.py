# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head

        # Count total nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # Dummy node to track new head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while count >= k:
            curr = prev.next
            next_node = curr.next
            
            # Reverse k nodes
            for _ in range(k - 1):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next

            prev = curr
            count -= k

        return dummy.next

    # Helper function to print the linked list (Python 2-compatible)
    def printList(self, head):
        while head:
            print head.val, "->",
            head = head.next
        print "None"


if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    solution.printList(new_head)
