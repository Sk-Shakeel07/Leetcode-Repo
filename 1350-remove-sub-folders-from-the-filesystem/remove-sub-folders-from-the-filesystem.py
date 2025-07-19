class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()  # sort lexicographically
        res = []
        for dir in folder:
            if not res or not dir.startswith(res[-1] + '/'):
                res.append(dir)
        return res
