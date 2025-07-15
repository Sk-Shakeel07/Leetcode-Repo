class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        for x in operations:
            if x == "+":
                res.append(res[-1] + res[-2])
            elif x == "D":
                res.append(2 * res[-1])
            elif x == "C":
                res.pop()
            else:
                res.append(int(x))
        return sum(res)
