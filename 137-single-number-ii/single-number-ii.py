class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0  # Track bits appearing once and twice

        for num in nums:
            ones = (ones ^ num) & ~twos  # XOR with num, but reset if in twos
            twos = (twos ^ num) & ~ones  # XOR with num, but reset if in ones
        
        return ones  # The single number remains in ones
