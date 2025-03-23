class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        
        // Step 1: Apply operations
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1] && nums[i] != 0) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        
        // Step 2: Shift zeros to the end using a for loop
        int index = 0; // Pointer for non-zero elements
        
        // Move non-zero elements forward
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[index++] = nums[i];
            }
        }
        
        // Fill the remaining positions with zeros
        for (int i = index; i < n; i++) {
            nums[i] = 0;
        }
        
        return nums;
    }
}
