class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split("/")  # Split the path by '/'

        for part in parts:
            if part == "..":
                if stack:  # If stack is not empty, pop the last directory
                    stack.pop()
            elif part and part != ".":  # Ignore empty parts and '.'
                stack.append(part)

        return "/" + "/".join(stack)  # Construct the canonical path


solution = Solution()
print(solution.simplifyPath("/home/")) 
print(solution.simplifyPath("/home//foo/"))  
print(solution.simplifyPath("/home/user/Documents/../Pictures"))  
print(solution.simplifyPath("/../"))  
print(solution.simplifyPath("/.../a/../b/c/../d/./"))  
