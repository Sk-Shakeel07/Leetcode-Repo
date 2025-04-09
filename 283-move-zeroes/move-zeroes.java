class Solution {
    public void moveZeroes(int[] nums) {
        int insertPos = 0;

        // First pass: move all non-zero elements to the front
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[insertPos] = nums[i];
                insertPos++;
            }
        }

        // Second pass: fill remaining positions with 0
        for (int i = insertPos; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
