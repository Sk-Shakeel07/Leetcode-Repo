class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for num in arr:
            new_cur = set()
            for x in cur:
                new_cur.add(num | x)
            new_cur.add(num)
            cur = new_cur
            res.update(cur)
        return len(res)
