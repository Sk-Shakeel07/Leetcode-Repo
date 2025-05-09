class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_length = 1
        count = 9
        start = 1

        # Step 1: Find the range where the nth digit falls
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number that contains the nth digit
        number = start + (n - 1) // digit_length

        # Step 3: Find the digit within the number
        digit_index = (n - 1) % digit_length
        return int(str(number)[digit_index])
