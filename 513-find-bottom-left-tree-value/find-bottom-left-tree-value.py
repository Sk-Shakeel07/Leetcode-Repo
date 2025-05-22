# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        last = 0
        q = deque([root])

        while q:
            count = len(q)
            for i in range(count):
                curr = q.popleft()
                if i == 0:
                    last = curr.val  # last leftMost val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return last