from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists) == 0:
            return None
        
        min_heap = []
        
        # Custom comparator for ListNode (since Python's heapq doesn't support direct ListNode comparison)
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        # Push the head nodes of each list into the heap
        for l in lists:
            if l:
                heappush(min_heap, Wrapper(l))
        
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            # Extract the smallest node
            node = heappop(min_heap).node
            curr.next = node
            curr = curr.next
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heappush(min_heap, Wrapper(node.next))
        
        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)


lists = [
    create_linked_list([1,4,5]),
    create_linked_list([1,3,4]),
    create_linked_list([2,6])
]

solution = Solution()
merged_list = solution.mergeKLists(lists)
print_linked_list(merged_list)
