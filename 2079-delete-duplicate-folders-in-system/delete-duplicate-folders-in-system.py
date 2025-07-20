from collections import defaultdict

class Node(object):
    def __init__(self):
        self.children = {}
        self.deleted = False

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        root = Node()
        
        # Build the tree structure
        for path in paths:
            curr = root
            for name in path:
                if name not in curr.children:
                    curr.children[name] = Node()
                curr = curr.children[name]
        
        # Encode each subtree and group nodes with identical structures
        mapping = defaultdict(list)
        self._encode(root, mapping)
        
        # Mark duplicate subtrees for deletion
        for group in mapping.values():
            if len(group) > 1:
                for node in group:
                    node.deleted = True
        
        # Collect all non-deleted paths
        result = []
        self._collect(root, [], result)
        return result
    
    def _encode(self, node, mapping):
        if not node.children:
            return "()"
        
        parts = []
        for name in sorted(node.children.keys()):
            child = node.children[name]
            sub = self._encode(child, mapping)
            parts.append(name + sub)
        
        sign = "(" + "".join(parts) + ")"
        mapping[sign].append(node)
        return sign
    
    def _collect(self, node, path, result):
        for name in node.children:
            child = node.children[name]
            if child.deleted:
                continue
            path.append(name)
            result.append(list(path))  # Create a shallow copy
            self._collect(child, path, result)
            path.pop()
