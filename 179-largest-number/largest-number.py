from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            else:
                return 1  # y should come before x

        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Sort with custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join sorted numbers
        result = ''.join(nums)
        
        # Handle edge case: if all are zeros, return "0"
        return '0' if result[0] == '0' else result

solution = Solution()
print(solution.largestNumber([10, 2])) 
print(solution.largestNumber([3, 30, 34, 5, 9]))  
print(solution.largestNumber([0, 0]))  
