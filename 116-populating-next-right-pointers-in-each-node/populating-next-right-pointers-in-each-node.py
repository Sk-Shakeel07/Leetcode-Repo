class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        leftmost = root  # Start at the root

        while leftmost.left:  # Traverse levels
            curr = leftmost
            while curr:  # Connect nodes within the level
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next  # Move to next node in the level
            
            leftmost = leftmost.left  # Move to next level

        return root
