class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Handle edge cases where there are no primes less than 2
        if n < 2:
            return 0
        
        # Initialize the 'is_prime' list where each index represents whether the number is prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        # Iterate through numbers from 2 up to the square root of n
        for i in xrange(2, int(n ** 0.5) + 1):
            if is_prime[i]:  # If i is prime, mark its multiples as non-prime
                for j in xrange(i * i, n, i):  # Start from i*i and mark multiples
                    is_prime[j] = False
        
        # Count the number of primes by summing up True values in 'is_prime'
        return sum(is_prime)
        
solution = Solution()
print solution.countPrimes(10) 
print solution.countPrimes(0)   
print solution.countPrimes(1)   
