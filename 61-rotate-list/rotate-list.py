# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute effective rotations
        k = k % length
        if k == 0:
            return head  # No change needed

        # Step 3: Find the new tail (length - k - 1th node)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Update pointers
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Connect last node to the first

        return new_head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val),
        current = current.next
        if current:
            print("->"),
    print("None")


if __name__ == "__main__":
    solution = Solution()

    
    arr1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(arr1)
    print("Original List:")
    print_linked_list(head1)
    rotated1 = solution.rotateRight(head1, 2)
    print("Rotated List:")
    print_linked_list(rotated1) 
    print("\n")

    
    arr2 = [0, 1, 2]
    head2 = create_linked_list(arr2)
    print("Original List:")
    print_linked_list(head2)
    rotated2 = solution.rotateRight(head2, 4)
    print("Rotated List:")
    print_linked_list(rotated2)  
'''
Approach -->
1>Edge Cases: Handle cases where head is None, has only one node, or k == 0.
2>Find Length: Traverse the list to get the total count of nodes.
3>Optimize Rotation: Since rotating N times results in the same list, use k = k % length.
4>Find New Tail: Locate the node at length - k - 1 position.
5>Rearrange Pointers: Set the new head, break the old tail, and link the end to the old head.
'''
