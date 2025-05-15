class Solution {
    public boolean circularArrayLoop(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            int slow, fast;
            slow = fast = i;
            boolean isForward = nums[i] > 0;
            
            while(true){
                slow = getNextIndex(nums, slow, isForward);
                if(slow == -1)
                    break;
                
                fast = getNextIndex(nums, fast, isForward);
                if(fast == -1)
                    break;
                
                fast = getNextIndex(nums, fast, isForward);
                if(fast == -1)
                    break;
                
                if(slow == fast)
                    return true;
            }
        }
        return false;
    }
    
    public int getNextIndex(int[] nums, int index, boolean curDirection){
        
        boolean direction = nums[index] >= 0;
        if(direction != curDirection) return -1; // Shold be either forward/backward direction.
        
        int nextIndex = (index + nums[index]) % nums.length;
        if(nextIndex < 0) nextIndex += nums.length;
        
        if(nextIndex == index) return -1; // to ignore case like [-1], [3,1,1] that have 1 element loop
        
        return nextIndex;
    }
}