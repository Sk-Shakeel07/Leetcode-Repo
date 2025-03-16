import java.util.*;
// Using Kadanes Algorithm
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE; // Stores the maximum sum found so far
        int currSum = 0; // Tracks the sum of the current subarray

        for (int i = 0; i < nums.length; i++) {
            currSum = Math.max(nums[i], currSum + nums[i]); // Start new subarray or extend current one
            maxSum = Math.max(maxSum, currSum); // Update max sum if needed
        }

        return maxSum; // Return the final maximum sum
    }
}

public class MaxSubarraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take input for array size
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] nums = new int[n];

        // Take input for array elements
        System.out.println("Enter the numbers in the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        // Create an instance of Solution and compute max subarray sum
        Solution solution = new Solution();
        int result = solution.maxSubArray(nums);

        // Print the maximum subarray sum
        System.out.println("The maximum sum is: " + result);

    }
}
