import java.util.Arrays;

class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums); // Step 1: Sort the array (O(n log n))
        
        int smallestMissing = 1; // The smallest missing positive number
        
        // Step 2: Iterate through the sorted array
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == smallestMissing) {
                smallestMissing++; // Move to the next expected positive number
            }
             else if (nums[i] > smallestMissing) {
                break; // If nums[i] is greater, return the current missing number
            }
        }
        
        return smallestMissing; // Return the first missing positive integer
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums1 = {1, 2, 0};
        System.out.println(sol.firstMissingPositive(nums1));

        int[] nums2 = {3, 4, -1, 1};
        System.out.println(sol.firstMissingPositive(nums2)); 
        int[] nums3 = {7, 8, 9, 11, 12};
        System.out.println(sol.firstMissingPositive(nums3)); 
    }
}
