class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int mid=nums[nums.length/2];
        int ans=0;
        for(int e:nums){
            ans+=(Math.abs(e-mid));
        }
        return ans;
    }
}