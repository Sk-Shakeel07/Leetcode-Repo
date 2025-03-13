class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Compute the area with the current left and right pointers
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            # Move the pointer that has the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area



if __name__ == "__main__":
    solution = Solution()
    
    
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height1))  

    
    height2 = [1, 1]
    print(solution.maxArea(height2)) 

    
    height3 = [4, 3, 2, 1, 4]
    print(solution.maxArea(height3))  

  
    height4 = [1, 2, 1]
    print(solution.maxArea(height4))  
