import heapq

class Solution(object):
    def kSmallestPairs(self, a, b, k):
        """
        :type a: List[int]
        :type b: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not a or not b:
            return []
        
        heap = []
        def push(i, j):
            if i < len(a) and j < len(b):
                heapq.heappush(heap, (a[i] + b[j], i, j))
        
        push(0, 0)
        pairs = []
        while heap and len(pairs) < k:
            _, i, j = heapq.heappop(heap)
            pairs.append([a[i], b[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs