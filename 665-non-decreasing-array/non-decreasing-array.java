class Solution {
    public boolean checkPossibility(int[] nums) {        
        // corner case
        if(nums == null || nums.length <= 1) return true;
        
        // the count of continuous non-decreasing sub-array
        int count = 1;
        int index = 0;
        
        int n = nums.length;        
        for(int i = 1; i < n; i++){
            if(nums[i] < nums[i - 1]){
                index = i;
                count++;
            }
        }
        
        if(count == 1) return true;
        if(count == 2){ 
            // if the discord happens at start or end position, we can modify
            // it to match the condition
            if(index == 1 || index == n - 1) return true;
            
            // if in the middle, we modify nums[index - 2]
            // index - 2, (index - 1, index) , index + 1
            if(nums[index + 1] >= nums[index - 1] || nums[index] >= nums[index - 2]) {
                return true;
            }
            return false;
        }
        
        return false;
    }
}