# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([(root, False)])  # (node, is_left)
        total_sum = 0

        while queue:
            node, is_left = queue.popleft()

            if is_left and not node.left and not node.right:
                total_sum += node.val

            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))

        return total_sum
