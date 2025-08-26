class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Collect and sort coordinates
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size)
        sorted_coords = sorted(coords)
        index = {x:i for i,x in enumerate(sorted_coords)}

        # Step 2: Track heights
        heights = [0] * len(sorted_coords)
        res = []
        max_h = 0

        # Step 3: Process squares
        for left, size in positions:
            l = index[left]
            r = index[left + size]
            base = max(heights[l:r])   # find current base height
            new_h = base + size
            for i in range(l, r):      # update covered range
                heights[i] = new_h
            max_h = max(max_h, new_h)
            res.append(max_h)
        
        return res
