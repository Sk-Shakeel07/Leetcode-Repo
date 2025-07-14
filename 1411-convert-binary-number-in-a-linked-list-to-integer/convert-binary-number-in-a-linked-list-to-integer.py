# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        ans = 0
        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans
