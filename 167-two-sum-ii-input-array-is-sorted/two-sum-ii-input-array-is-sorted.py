class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1  # Initialize two pointers
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based index
            elif current_sum < target:
                left += 1  # Move left pointer right to increase sum
            else:
                right -= 1  # Move right pointer left to decrease sum
        
        return []  # This will never be reached as one solution is guaranteed
