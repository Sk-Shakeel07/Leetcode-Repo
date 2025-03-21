class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                result.append(".".join(path))
                return
            if len(path) >= 4:
                return
            
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                    continue
                backtrack(end, path + [segment])

        result = []
        backtrack(0, [])
        return result

sol = Solution()
print(sol.restoreIpAddresses("25525511135"))  
print(sol.restoreIpAddresses("0000")) 
print(sol.restoreIpAddresses("101023"))  
