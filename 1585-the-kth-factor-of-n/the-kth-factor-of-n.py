import math

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        
        # Find factors from 1 to sqrt(n)
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)  # i is a factor
                if i != n // i:
                    factors.append(n // i)  # n // i is also a factor
        
        # Sort the factors in ascending order
        factors.sort()
        
        # Return the kth factor, or -1 if not enough factors
        return factors[k - 1] if k <= len(factors) else -1
