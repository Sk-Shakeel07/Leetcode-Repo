import collections

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.val = None
        self.is_leaf = False
        
    def set_val(self, val):
        self.val = val
        
    def set_leaf(self):
        self.is_leaf = True
        

class MapSum(object):

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        curr = self.trie
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.set_val(val)
        curr.set_leaf()

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.trie
        sum_prefix = 0
        
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        
        if curr.is_leaf:
            sum_prefix += curr.val
        
        queue = collections.deque([curr])
        while queue:
            curr = queue.popleft()
            for child in curr.children:
                node = curr.children[child]
                queue.append(node)
                if node.is_leaf:
                    sum_prefix += node.val
                    
        return sum_prefix


# Example usage in Python 2
# obj = MapSum()
# obj.insert("apple", 3)
# print(obj.sum("ap"))  # Output: 3
