from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            prev = None
            
            for _ in range(size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            prev.next = None  # Last node in the level points to NULL
        
        return root
