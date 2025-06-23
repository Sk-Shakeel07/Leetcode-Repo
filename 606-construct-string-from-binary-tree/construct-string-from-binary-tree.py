# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        res = []
        self.dfs(root, res)
        return ''.join(res)

    def dfs(self, root, res):
        if root is None:
            return

        res.append(str(root.val))

        if root.left is None and root.right is None:
            return

        res.append('(')
        self.dfs(root.left, res)
        res.append(')')

        if root.right is not None:
            res.append('(')
            self.dfs(root.right, res)
            res.append(')')