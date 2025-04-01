class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= (n - 1)  # Clear the lowest set bit
            count += 1
        return count

sol = Solution()
print(sol.hammingWeight(11))        
print(sol.hammingWeight(128))       
print(sol.hammingWeight(2147483645)) 
